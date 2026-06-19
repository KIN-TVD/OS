from fastapi import APIRouter
from src.routers import drafts_router
from src.routers.missions import router as missions_router
from src.routers.publish import router as publish_router
from src.routers.knowledge import router as knowledge_router
from src.routers.evaluations import router as evaluations_router
from src.routers.outputs import router as outputs_router
from src.routers.settings import router as settings_router
from src.routers.dashboard import router as dashboard_router
from src.routers.history import router as history_router

api_router = APIRouter()

# Health check
@api_router.get("/health")
def health_check():
    return {"status": "ok", "message": "AgentOS API is running"}

# Mount routers
api_router.include_router(drafts_router)
api_router.include_router(missions_router)
api_router.include_router(publish_router)
api_router.include_router(knowledge_router)
api_router.include_router(evaluations_router)
api_router.include_router(outputs_router)
api_router.include_router(settings_router)
api_router.include_router(dashboard_router)
api_router.include_router(history_router)
