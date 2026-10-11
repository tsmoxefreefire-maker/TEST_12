"""🆕 batch 42 · THE DATABASE (Hareth + the engineer: «نولّد قبل، ونحفظ، ونعرض فوراً» · and Render's free disk that forgets
everything at every restart).

ONE PostgreSQL, given by the environment variable DATABASE_URL (Render, Supabase, the company's own server… never in GitHub).
It does two jobs:
  1. KEEP  (table ie_files): every file the server writes under data/ (books, lessons, graphs, the Lego / identity / place
     libraries, the model's scenes) is copied into the database after each change (save_files), and copied back when the
     server starts with an empty disk (restore_files). The factory keeps working on files (fast, its code unchanged);
     the database is the copy that never disappears.
  2. FIND  (table ie_scenes): one row per scene, made BEFORE any student asks: the questions it answers (description),
     its JSON, and its meaning-numbers (embedding). core/scene_index.py fills it and searches it.
No DATABASE_URL → everything works exactly as before (files only), and the scene rows live in data/scene_index.json.
Only standard SQL (no extension to install). Driver: psycopg (requirements.txt), imported only when a database is set."""
import base64
import hashlib
import json
import os
import threading

from core import settings

_LOCK = threading.RLock()
_CONN = None
_MANIFEST = {}                    # path → sha of what the database holds (so only CHANGED files are sent)
_READY = False

SCHEMA = [
    """CREATE TABLE IF NOT EXISTS ie_files (
         path text PRIMARY KEY, body text NOT NULL, sha text NOT NULL, updated_at timestamptz NOT NULL DEFAULT now())""",
    """CREATE TABLE IF NOT EXISTS ie_scenes (
         id text PRIMARY KEY, book_id text NOT NULL, lesson_id text NOT NULL, concept_id text NOT NULL DEFAULT '',
         position int NOT NULL DEFAULT 0, kind text NOT NULL, name text NOT NULL DEFAULT '', lesson_title text NOT NULL DEFAULT '',
         stage text, grade int, subject text, questions jsonb NOT NULL, description text NOT NULL, scene jsonb NOT NULL,
         source text NOT NULL DEFAULT 'factory', approved boolean NOT NULL DEFAULT true, version text NOT NULL,
         emb real[], emb_model text, updated_at timestamptz NOT NULL DEFAULT now())""",
    "CREATE INDEX IF NOT EXISTS ie_scenes_book ON ie_scenes (book_id)",
    "CREATE INDEX IF NOT EXISTS ie_scenes_concept ON ie_scenes (concept_id)",
]
ROW = ("id", "book_id", "lesson_id", "concept_id", "position", "kind", "name", "lesson_title", "stage", "grade", "subject",
       "questions", "description", "source", "approved", "version")


def url() -> str:
    return os.environ.get("DATABASE_URL", "").strip()


def enabled() -> bool:
    return bool(url())


def where() -> str:
    """for /health and the docs: where things are kept (never the address itself: it holds a password)."""
    return "postgres" if enabled() else "files"


# ---------- the connection ----------
def _connect():
    import psycopg                                                    # only when a database is set
    return psycopg.connect(url(), autocommit=True)


def run(sql: str, params=None):
    """one statement; reconnects once if the connection dropped (the database restarted, the network blinked)."""
    global _CONN, _READY
    with _LOCK:
        for attempt in (1, 2):
            try:
                if _CONN is None or getattr(_CONN, "closed", False):
                    _CONN = _connect()
                    _READY = False
                if not _READY:
                    for s in SCHEMA:
                        _CONN.execute(s)
                    _READY = True
                return _CONN.execute(sql, params)
            except Exception as e:                                    # a dead connection → one fresh try; a wrong SQL → raised
                if attempt == 2 or "closed" not in str(e).lower() and "connection" not in str(e).lower():
                    raise
                try:
                    _CONN.close()
                except Exception:
                    pass
                _CONN = None


def close():
    global _CONN
    with _LOCK:
        if _CONN is not None:
            try:
                _CONN.close()
            finally:
                _CONN = None


# ---------- 1. KEEP: data/ ⇄ ie_files ----------
def _files(root):
    for d, _, names in os.walk(root):
        for n in names:
            if n.endswith((".tmp", ".lock")):
                continue
            p = os.path.join(d, n)
            yield os.path.relpath(p, root).replace(os.sep, "/"), p


def _pack(raw: bytes) -> str:
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return "b64:" + base64.b64encode(raw).decode()


def _unpack(body: str) -> bytes:
    return base64.b64decode(body[4:]) if body.startswith("b64:") else body.encode("utf-8")


def _sha(p: str) -> str:
    with open(p, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()


def restore_files(root: str = None) -> int:
    """the server starts: every kept file that is missing (or different) on the disk is written back. → how many."""
    if not enabled():
        return 0
    root = root or settings.DATA_DIR
    n = 0
    with _LOCK:
        _MANIFEST.clear()
        for path, body, sha in run("SELECT path, body, sha FROM ie_files").fetchall():
            _MANIFEST[path] = sha
            p = os.path.join(root, *path.split("/"))
            if os.path.abspath(p).startswith(os.path.abspath(root) + os.sep):        # never outside data/
                raw = _unpack(body)
                if not os.path.exists(p) or _sha(p) != sha:
                    os.makedirs(os.path.dirname(p), exist_ok=True)
                    with open(p, "wb") as f:
                        f.write(raw)
                    n += 1
    return n


def save_files(root: str = None) -> dict:
    """after a change: the files that are new or changed go to the database; the ones deleted from the disk leave it."""
    if not enabled():
        return {"saved": 0, "removed": 0}
    root = root or settings.DATA_DIR
    saved = removed = 0
    with _LOCK:
        if not _MANIFEST:
            _MANIFEST.update({p: s for p, s in run("SELECT path, sha FROM ie_files").fetchall()})
        here = {}
        for rel, p in _files(root):
            if rel == "scene_index.json":                                 # (the file copy of the scene rows: the database has its own table)
                continue
            with open(p, "rb") as f:
                raw = f.read()
            sha = hashlib.sha1(raw).hexdigest()
            here[rel] = sha
            if _MANIFEST.get(rel) != sha:
                run("INSERT INTO ie_files (path, body, sha, updated_at) VALUES (%s, %s, %s, now()) "
                    "ON CONFLICT (path) DO UPDATE SET body = EXCLUDED.body, sha = EXCLUDED.sha, updated_at = now()", [rel, _pack(raw), sha])
                _MANIFEST[rel] = sha
                saved += 1
        for rel in [r for r in _MANIFEST if r not in here]:
            run("DELETE FROM ie_files WHERE path = %s", [rel])
            _MANIFEST.pop(rel, None)
            removed += 1
    return {"saved": saved, "removed": removed}


# ---------- 2. FIND: the scene rows (the database, or a file when there is none) ----------
class _PgScenes:
    def versions(self, book_id: str) -> dict:
        return {i: (v, m) for i, v, m in run("SELECT id, version, emb_model FROM ie_scenes WHERE book_id = %s", [book_id]).fetchall()}

    def upsert(self, row: dict, scene: dict):
        run("INSERT INTO ie_scenes (" + ", ".join(ROW) + ", scene, emb, emb_model, updated_at) VALUES ("
            + ", ".join("%s::jsonb" if c == "questions" else "%s" for c in ROW) + ", %s::jsonb, NULL, NULL, now()) "
            "ON CONFLICT (id) DO UPDATE SET " + ", ".join(f"{c} = EXCLUDED.{c}" for c in ROW[1:])
            + ", scene = EXCLUDED.scene, emb = NULL, emb_model = NULL, updated_at = now()",
            [json.dumps(row[c], ensure_ascii=False) if c == "questions" else row[c] for c in ROW] + [json.dumps(scene, ensure_ascii=False)])

    def upsert_many(self, pairs):
        for row, scene in pairs:
            self.upsert(row, scene)

    def set_embs(self, items):
        for i, vec, model in items:
            self.set_emb(i, vec, model)

    def delete(self, ids):
        for i in ids:
            run("DELETE FROM ie_scenes WHERE id = %s", [i])

    def delete_book(self, book_id: str):
        run("DELETE FROM ie_scenes WHERE book_id = %s", [book_id])

    def set_emb(self, i: str, vec, model: str):
        run("UPDATE ie_scenes SET emb = %s::real[], emb_model = %s WHERE id = %s", [[float(round(x, 6)) for x in vec], model, i])

    def all_rows(self) -> list:
        cols = ROW + ("emb", "emb_model")
        return [dict(zip(cols, r)) for r in run("SELECT " + ", ".join(cols) + " FROM ie_scenes ORDER BY book_id, lesson_id, concept_id, position").fetchall()]

    def scenes(self, ids) -> dict:
        return {i: sc for i, sc in run("SELECT id, scene FROM ie_scenes WHERE id = ANY(%s::text[])", [list(ids)]).fetchall()} if ids else {}

    def stamp(self) -> str:
        n, t = run("SELECT count(*), coalesce(max(updated_at)::text, '') FROM ie_scenes").fetchone()
        return f"{n}|{t}"

    # 🆕 batch 43: the search works inside ONE book (the student's) → only that book's rows are read
    def book_rows(self, book_id: str) -> list:
        cols = ROW + ("emb", "emb_model")
        return [dict(zip(cols, r)) for r in run("SELECT " + ", ".join(cols) + " FROM ie_scenes WHERE book_id = %s ORDER BY lesson_id, concept_id, position",
                                                [book_id]).fetchall()]

    def book_stamp(self, book_id: str) -> str:
        n, t = run("SELECT count(*), coalesce(max(updated_at)::text, '') FROM ie_scenes WHERE book_id = %s", [book_id]).fetchone()
        return f"{n}|{t}"

    def counts(self, model) -> dict:
        n, b, e = run("SELECT count(*), count(DISTINCT book_id), count(*) FILTER (WHERE emb_model = %s) FROM ie_scenes", [model or ""]).fetchone()
        return {"rows": n, "books": b, "embedded": e}


class _FileScenes:
    """the same, in data/scene_index.json (no database): fine for a laptop, a test, or a few books."""
    def _path(self):
        return os.path.join(settings.DATA_DIR, "scene_index.json")

    _memo = {}

    def _load(self) -> dict:
        try:
            m = os.path.getmtime(self._path())
            if self._memo.get("path") == self._path() and self._memo.get("m") == m:
                return self._memo["d"]                                    # (read once until the file changes)
            with open(self._path(), encoding="utf-8") as f:
                d = json.load(f)
            _FileScenes._memo = {"path": self._path(), "m": m, "d": d}
            return d
        except (OSError, ValueError):
            return {}

    def _save(self, d: dict):
        os.makedirs(settings.DATA_DIR, exist_ok=True)
        tmp = self._path() + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)
        os.replace(tmp, self._path())
        _FileScenes._memo = {"path": self._path(), "m": os.path.getmtime(self._path()), "d": d}

    def versions(self, book_id):
        return {i: (r["version"], r.get("emb_model")) for i, r in self._load().items() if r["book_id"] == book_id}

    def upsert(self, row, scene):
        with _LOCK:
            d = dict(self._load())
            d[row["id"]] = dict(row, scene=scene, emb=None, emb_model=None)
            self._save(d)

    def upsert_many(self, pairs):
        with _LOCK:
            d = dict(self._load())
            for row, scene in pairs:
                d[row["id"]] = dict(row, scene=scene, emb=None, emb_model=None)
            self._save(d)

    def set_embs(self, items):
        with _LOCK:
            d = dict(self._load())
            for i, vec, model in items:
                if i in d:
                    d[i] = dict(d[i], emb=[round(float(x), 6) for x in vec], emb_model=model)
            self._save(d)

    def delete(self, ids):
        if not ids:
            return
        with _LOCK:
            d = dict(self._load())
            for i in ids:
                d.pop(i, None)
            self._save(d)

    def delete_book(self, book_id):
        with _LOCK:
            self._save({i: r for i, r in self._load().items() if r["book_id"] != book_id})

    def set_emb(self, i, vec, model):
        with _LOCK:
            d = dict(self._load())
            if i in d:
                d[i] = dict(d[i], emb=[round(float(x), 6) for x in vec], emb_model=model)
                self._save(d)

    def all_rows(self):
        return sorted(({k: v for k, v in r.items() if k != "scene"} for r in self._load().values()),
                      key=lambda r: (r["book_id"], r["lesson_id"], r["concept_id"], r["position"]))

    def scenes(self, ids):
        d = self._load()
        return {i: d[i]["scene"] for i in ids if i in d}

    def stamp(self):
        try:
            return f"{self._path()}|{os.path.getmtime(self._path())}"
        except OSError:
            return f"{self._path()}|0"

    def book_rows(self, book_id):
        return [r for r in self.all_rows() if r["book_id"] == book_id]

    def book_stamp(self, book_id):
        return self.stamp()

    def counts(self, model):
        rows = self._load().values()
        return {"rows": len(rows), "books": len({r["book_id"] for r in rows}), "embedded": sum(1 for r in rows if model and r.get("emb_model") == model)}


def scenes():
    """the scene rows' home: the database when there is one, else a file."""
    return _PgScenes() if enabled() else _FileScenes()
