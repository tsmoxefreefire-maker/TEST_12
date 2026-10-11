"""The endpoints. Each one is THIN: it calls the service and turns its errors into HTTP codes (NotFound → 404, BadInput → 400)."""
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse, Response

from api.schemas import (AskRequest, BookSummary, BrowserReport, GenerateRequest, GenerateResponse, Health, LegoChoice, LessonSummary, LLMSceneRequest,
                         LLMSceneResponse, LLMSceneSummary, ReviewRequest)
from core import contract, llm_scenes, service, settings

router = APIRouter()


def _call(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except (service.NotFound, llm_scenes.NotFound) as e:
        raise HTTPException(status_code=404, detail=str(e))
    except (service.BadInput, llm_scenes.BadInput) as e:
        raise HTTPException(status_code=400, detail=str(e))


def _write(fn, *args, book_id=None, **kwargs):
    """🆕 batch 42: a call that CHANGES something → afterwards everything changed goes into the database (Render's disk forgets)."""
    out = _call(fn, *args, **kwargs)
    service.persist(book_id)
    return out


@router.get("/health", response_model=Health, tags=["system"])
def health():
    from core import db
    return {"status": "ok", "version": settings.API_VERSION, "storage": db.where()}


# ---------- 🆕 batch 42 · ask a question → the scene at once ----------
@router.get("/ask", response_class=HTMLResponse, tags=["ask"])
def ask_page():
    """A small page: write a question, the scene that answers it opens at once (to try the search by hand)."""
    service.ensure_samples()
    return HTMLResponse(content=_call(service.ask_html))


@router.post("/ask", tags=["ask"])
def ask(req: AskRequest) -> Dict[str, Any]:
    """A student's question → the concept's scenes (the cartoon first) + which one answers best + a link that opens the page there.
    How it found it («how»): name (the concept's name is in the question) · meaning (a meaning model, if set) · text (the closest spelling).
    🆕 batch 43: ONLY inside the student's book (book_id required) · his lesson first · a question outside his book → found=false,
    a message («خلينا نرجع لـ…») and «back»: the link to the concept he is studying (never a scene from another book)."""
    return _call(service.ask, req.question, req.book_id, req.grade, req.stage, req.lesson_id, req.concept_id)


@router.get("/search/status", tags=["ask"])
def search_status() -> Dict[str, Any]:
    """Where the rows are kept (postgres / files), how many scenes can be found, and which meaning model (if any)."""
    return _call(service.search_status)


@router.post("/search/reindex", tags=["ask"])
def search_reindex(book_id: Optional[str] = Query(None, description="كتاب واحد (فاضي = كل الكتب)")) -> List[Dict[str, Any]]:
    """Make the search rows again (only the changed scenes are written and given meaning-numbers)."""
    return _call(service.reindex, book_id)


# ---------- 📖 the PAGE: the same interactive page as the published one, for ANY graph on the server ----------
@router.get("/tts/status", tags=["voice"])
def tts_status() -> Dict[str, Any]:
    """🔊 batch 44: is the voice on, who speaks, how many lines are already made."""
    return _call(service.tts_status)


@router.get("/tts", tags=["voice"])
def tts(text: str = Query(..., description="سطر الشرح زي ما الطالب بيقرأه"),
        stage: str = Query("kids", description="kids · junior · teen · senior (أبطأ للصغار)")):
    """🔊 batch 44: one line read aloud (made once by the model, then always from the saved file)."""
    data, mime = _call(service.tts_audio, text, stage)
    return Response(content=data, media_type=mime, headers={"Cache-Control": "public, max-age=604800"})


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    """The server's front page: the books, and a box to send a new graph."""
    service.ensure_samples()
    return HTMLResponse(content=_call(service.home_html))


@router.get("/explain", response_class=HTMLResponse, tags=["page"])
def explain_page(books: Optional[str] = Query(None, description="كتب معيّنة: b1,b2 (فاضي = كل الكتب)")):
    """The interactive page with every book on the server (scenes, the 5 activities, films, sounds per subject and age)."""
    service.ensure_samples()
    ids = [b.strip() for b in books.split(",")] if books else None
    return HTMLResponse(content=_call(service.page_html, ids))


@router.get("/explain/{book_id}", response_class=HTMLResponse, tags=["page"])
def explain_book_page(book_id: str):
    """The interactive page of ONE book (e.g. the one you just sent with /explanations/generate → its «page_url»)."""
    return HTMLResponse(content=_call(service.page_html, [book_id]))


@router.get("/explain-data", tags=["page"])
def explain_data(books: Optional[str] = Query(None, description="b1,b2 (فاضي = كل الكتب)")) -> Dict[str, Any]:
    """Exactly what the page receives (for a front end that wants to draw the page itself)."""
    service.ensure_samples()
    ids = [b.strip() for b in books.split(",")] if books else None
    return _call(service.page_data, ids)


@router.get("/scene-kinds", tags=["contract"])
def scene_kinds() -> Dict[str, Any]:
    """The contract: every scene kind, what it means and its fields (for the front end)."""
    return contract.describe()


@router.post("/explanations/generate", response_model=GenerateResponse, tags=["explanations"])
def generate(req: GenerateRequest):
    """Graph → explanations for every lesson (kept on the server; generated once, then served instantly)."""
    return _call(service.generate, graph=req.graph, graph_path=req.graph_path, use_llm=req.use_llm,
                 lesson_text=req.lesson_text, subject=req.subject, grade=req.grade)   # (it saves into the database itself)


@router.post("/explanations/samples", response_model=List[GenerateResponse], tags=["explanations"])
def samples(force: bool = Query(False, description="true = اعملهم كلهم من جديد")):
    """Make the 12 sample books (grade 4 → 12) on the server."""
    return _call(service.seed_samples, force=force in (True, "true", "1", 1))


@router.get("/books", response_model=List[BookSummary], tags=["explanations"])
def books():
    service.ensure_samples()
    return service.list_books()


@router.delete("/books/{book_id}", tags=["explanations"])
def delete_book(book_id: str) -> Dict[str, Any]:
    """Remove a book from the server (its explanations and its graph)."""
    return _call(service.delete_book, book_id)   # (it saves into the database itself)


@router.get("/books/{book_id}/lessons", response_model=List[LessonSummary], tags=["explanations"])
def lessons(book_id: str):
    return _call(service.list_lessons, book_id)


@router.get("/lessons/{lesson_id}/explanation", tags=["explanations"])
def lesson_explanation(lesson_id: str, book_id: Optional[str] = Query(None),
                       include_llm: bool = Query(False, description="زيد المشاهد اللي كتبها الموديل وانقبلت من المعلم")) -> Dict[str, Any]:
    """All the scenes of one lesson + texts + picture URLs + «audience» (the age stage). See /scene-kinds for the fields."""
    return _call(service.get_lesson, lesson_id, book_id, include_llm=include_llm)


@router.get("/concepts/{concept_id}/explanation", tags=["explanations"])
def concept_explanation(concept_id: str, book_id: Optional[str] = Query(None)) -> Dict[str, Any]:
    return _call(service.get_concept, concept_id, book_id)


# ---------- 🧱 Lego drawings (batch 29): a concept with no drawing gets one BUILT from our parts ----------
@router.get("/lego/parts", tags=["lego"])
def lego_parts() -> Dict[str, Any]:
    """The parts (main + badges + motions) and what each can mean — the same list the model chooses from."""
    return service.lego_parts()


@router.get("/lego/drawings", tags=["lego"])
def lego_drawings() -> List[Dict[str, Any]]:
    """Every drawing built so far (the library that grows): its picture, the model's other suggestions, and its status
    (auto = the model's first choice, used now · approved = a teacher picked it · rejected = back to the subject character)."""
    return service.lego_library()


@router.post("/lego/drawings/choose", tags=["lego"])
def lego_choose(req: LegoChoice) -> Dict[str, Any]:
    """The teacher picks another suggestion (pick) or says no (reject). The saved books show the change at once."""
    return _write(service.lego_choose, req.name, req.pick, req.reject)


@router.get("/art/{key}.svg", tags=["art"])
def art_svg(key: str, stage: str = Query("kids", description="kids · junior · teen · senior (the face changes with the age)")):
    """A character as SVG (the key comes from «icons»/«art» in the lesson; URL-encoded). It carries its own face rules."""
    svg = _call(service.get_art, key, stage)
    return Response(content=svg, media_type="image/svg+xml", headers={"Cache-Control": "public, max-age=86400"})


# ---------- 🤖 scenes written by the model (with our template's toolkit) ----------
@router.post("/llm/scenes/generate", response_model=LLMSceneResponse, tags=["llm scenes"])
def llm_generate(req: LLMSceneRequest):
    """The model writes a NEW scene for a concept, with our toolkit (SDK). Checked automatically; waits for a teacher (pending_review)."""
    return _write(llm_scenes.generate, req.book_id, req.lesson_id, concept_id=req.concept_id, idea=req.idea,
                  max_scenes=req.max_scenes, force=req.force)


@router.get("/llm/scenes", response_model=List[LLMSceneSummary], tags=["llm scenes"])
def llm_list(book_id: Optional[str] = Query(None), lesson_id: Optional[str] = Query(None), status: Optional[str] = Query(None)):
    return _call(llm_scenes.list_scenes, book_id, lesson_id, status)


@router.get("/llm/scenes/{scene_id}", tags=["llm scenes"])
def llm_get(scene_id: str, book_id: Optional[str] = Query(None)) -> Dict[str, Any]:
    """Everything about one scene: the code, the checks, the data the model got, the review."""
    return _call(llm_scenes.get_scene, scene_id, book_id)


@router.get("/llm/scenes/{scene_id}/runner.html", response_class=HTMLResponse, tags=["llm scenes"])
def llm_runner(scene_id: str, book_id: Optional[str] = Query(None)):
    """The sandbox page. Use it ONLY inside <iframe sandbox="allow-scripts"> (its CSP blocks every network request)."""
    html = _call(llm_scenes.runner, scene_id, book_id)
    return HTMLResponse(content=html, headers={"Content-Security-Policy": "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; sandbox allow-scripts"})


@router.post("/llm/scenes/{scene_id}/review", response_model=LLMSceneSummary, tags=["llm scenes"])
def llm_review(scene_id: str, req: ReviewRequest, book_id: Optional[str] = Query(None)):
    """The teacher approves (students will see it) or rejects."""
    out = _call(llm_scenes.review, scene_id, req.approve, req.note, book_id)
    service.persist(llm_scenes.get_scene(scene_id, book_id)["book_id"])   # 🆕 batch 42: an approved scene is found by a question too
    return out


@router.post("/llm/scenes/{scene_id}/report", tags=["llm scenes"])
def llm_report(scene_id: str, req: BrowserReport, book_id: Optional[str] = Query(None)) -> Dict[str, Any]:
    """What the browser saw when the scene ran (sent by the preview page): drew? everything inside? errors?"""
    return _write(llm_scenes.report, scene_id, req.model_dump(), book_id)


@router.get("/llm/sdk", tags=["llm scenes"])
def llm_sdk() -> Dict[str, Any]:
    """What the model may use (the toolkit), the rules per age, what is forbidden, an example, and how to embed the sandbox."""
    return llm_scenes.sdk_doc()
