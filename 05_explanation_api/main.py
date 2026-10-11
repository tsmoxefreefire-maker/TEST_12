"""The door of the service: creates the FastAPI app and plugs in the endpoints.
Run:  uvicorn main:app --reload  → open http://127.0.0.1:8000/  (the books + send a graph) · /explain (the page) · /ask (ask a question) · /docs
🆕 batch 42: set DATABASE_URL (PostgreSQL) on the server and nothing is lost when it restarts; without it, files only (as before)."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from core import service, settings

TAGS = [   # 🆕 batch 31: the groups in /docs, explained (a more professional API page)
    {"name": "explanations", "description": "ابعت جراف ← الشرح كامل بينعمل وبينحفظ · الكتب والدروس والمفاهيم."},
    {"name": "page", "description": "الصفحة التفاعلية نفسها (`/explain`) والداتا (`/explain-data`) لأي فرونت إند."},
    {"name": "art", "description": "رسومات الشخصيات كـ SVG (نفس رسومات الصفحة)."},
    {"name": "lego", "description": "🧱 رسومات بتنركّب من قطع للمفاهيم اللي ما إلها رسمة · مكتبتها واختيار المعلم."},
    {"name": "ask", "description": "🆕 سؤال الطالب ← المشهد اللي بيجاوبه فوراً (المشاهد معمولة قبل: ولا توليد والطالب بيستنى)."},
    {"name": "llm scenes", "description": "🤖 (اختياري) مشهد بيكتبه الموديل · بيطلع للطالب بس بعد موافقة المعلم."},
    {"name": "contract", "description": "أنواع المشاهد والقواعد."},
    {"name": "system", "description": "حالة السيرفر ونسخته."},
]
app = FastAPI(title="Interactive Explanation API · الشرح التفاعلي", version=settings.API_VERSION, openapi_tags=TAGS,
              description="بياخد أي جراف وبيعمل الشرح التفاعلي كامل: الصفحة نفسها (/explain) بكل التفاعلات والأصوات، "
                          "والداتا (JSON) ورسومات الشخصيات (SVG) لأي فرونت إند. المادة الجديدة بتاخد هوية خاصة فيها (صوت وشخصيات).")
app.add_middleware(CORSMiddleware, allow_origins=settings.CORS_ORIGINS, allow_methods=["*"], allow_headers=["*"])
app.include_router(router)
BOOT = service.boot()          # 🆕 batch 42: the server starts → what the database keeps comes back to the disk (Render forgets it at every restart)
