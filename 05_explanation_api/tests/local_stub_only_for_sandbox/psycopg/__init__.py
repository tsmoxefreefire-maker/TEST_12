"""LOCAL STUB of psycopg (connect / execute / fetchone / fetchall only) to run the database tests HERE against a REAL local
PostgreSQL — NOT shipped. The real thing on the server: pip install "psycopg[binary]" (it is in requirements.txt).

It speaks the PostgreSQL wire protocol (v3, simple queries) with «trust» login (a local test server only), and puts the
parameters into the SQL as quoted literals. The service code only uses what both have in common:
    conn = psycopg.connect(url, autocommit=True); conn.execute(sql, params).fetchall(); conn.close()
with %s placeholders, and json / arrays passed as text with a cast in the SQL (…%s::jsonb, …%s::real[])."""
import json
import socket
import struct
import urllib.parse

__version__ = "stub"


class Error(Exception):
    pass


class OperationalError(Error):
    pass


def _lit(v):
    """A Python value → an SQL literal (what psycopg would send as a parameter)."""
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, (list, tuple)):
        return "'{" + ",".join("NULL" if x is None else str(x) for x in v) + "}'"
    return "'" + str(v).replace("'", "''") + "'"


def _fill(sql, params):
    if not params:
        return sql
    out, i, it = [], 0, iter(params)
    while i < len(sql):
        if sql.startswith("%%", i):
            out.append("%"); i += 2
        elif sql.startswith("%s", i):
            out.append(_lit(next(it))); i += 2
        else:
            out.append(sql[i]); i += 1
    return "".join(out)


def _arr(text, cast):
    body = text.strip("{}")
    return [] if not body else [None if x == "NULL" else cast(x) for x in body.split(",")]


_CAST = {16: lambda s: s == "t", 20: int, 21: int, 23: int, 700: float, 701: float, 1700: float, 114: json.loads, 3802: json.loads,
         1021: lambda s: _arr(s, float), 1022: lambda s: _arr(s, float), 1007: lambda s: _arr(s, int), 1016: lambda s: _arr(s, int),
         1009: lambda s: _arr(s, str)}


class Cursor:
    def __init__(self, rows, status):
        self._rows, self.statusmessage = rows, status
        self.rowcount = len(rows) if rows else (int(status.split()[-1]) if status and status.split()[-1].isdigit() else -1)

    def fetchall(self):
        return list(self._rows)

    def fetchone(self):
        return self._rows[0] if self._rows else None


class Connection:
    def __init__(self, url):
        u = urllib.parse.urlsplit(url)
        self.closed = False
        try:
            self.s = socket.create_connection((u.hostname or "127.0.0.1", u.port or 5432), timeout=30)
        except OSError as e:
            raise OperationalError(str(e))
        user, db = urllib.parse.unquote(u.username or "postgres"), (u.path or "/postgres").lstrip("/") or "postgres"
        body = struct.pack("!i", 196608) + b"user\0" + user.encode() + b"\0database\0" + db.encode() + b"\0\0"
        self.s.sendall(struct.pack("!i", len(body) + 4) + body)
        while True:
            t, m = self._msg()
            if t == b"R" and struct.unpack("!i", m[:4])[0] != 0:
                raise OperationalError("the local test stub only logs in with «trust»")
            if t == b"E":
                raise OperationalError(self._err(m))
            if t == b"Z":
                break

    def _read(self, n):
        b = b""
        while len(b) < n:
            c = self.s.recv(n - len(b))
            if not c:
                raise OperationalError("the server closed the connection")
            b += c
        return b

    def _msg(self):
        t = self._read(1)
        n = struct.unpack("!i", self._read(4))[0]
        return t, self._read(n - 4)

    @staticmethod
    def _err(m):
        f = {p[:1]: p[1:].decode("utf-8", "replace") for p in m.split(b"\0") if p}
        return f.get(b"M", "error") + (f" ({f[b'D']})" if b"D" in f else "")

    def execute(self, sql, params=None):
        q = _fill(sql, params).encode("utf-8") + b"\0"
        self.s.sendall(b"Q" + struct.pack("!i", len(q) + 4) + q)
        rows, types, status, err = [], [], "", None
        while True:
            t, m = self._msg()
            if t == b"T":
                n, pos, types = struct.unpack("!h", m[:2])[0], 2, []
                for _ in range(n):
                    end = m.index(b"\0", pos)
                    types.append(struct.unpack("!i", m[end + 7:end + 11])[0])
                    pos = end + 19
            elif t == b"D":
                n, pos, row = struct.unpack("!h", m[:2])[0], 2, []
                for k in range(n):
                    ln = struct.unpack("!i", m[pos:pos + 4])[0]; pos += 4
                    if ln < 0:
                        row.append(None); continue
                    v = m[pos:pos + ln].decode("utf-8"); pos += ln
                    row.append(_CAST.get(types[k], str)(v))
                rows.append(tuple(row))
            elif t == b"C":
                status = m.rstrip(b"\0").decode()
            elif t == b"E":
                err = self._err(m)
            elif t == b"Z":
                break
        if err:
            raise Error(err)
        return Cursor(rows, status)

    def close(self):
        if not self.closed:
            try:
                self.s.sendall(b"X" + struct.pack("!i", 4)); self.s.close()
            except OSError:
                pass
            self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()


def connect(url, autocommit=True, **kw):
    return Connection(url)
