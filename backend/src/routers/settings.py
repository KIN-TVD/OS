from fastapi import APIRouter
from src.config.settings import settings

router = APIRouter(prefix="/settings", tags=["Settings"])

@router.get("/")
def get_settings():
    """Lấy cấu hình hiện tại (ẩn bớt các ký tự của API Key)"""
    def mask_key(k: str) -> str:
        if not k: return ""
        if len(k) <= 8: return "********"
        return f"{k[:4]}...{k[-4:]}"
        
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "dify_api_url": settings.dify_api_url,
        "dify_api_key": mask_key(settings.dify_api_key),
        "nvidia_api_key": mask_key(settings.nvidia_api_key),
        "gemini_api_key": mask_key(settings.gemini_api_key),
        "instagram_user_id": settings.instagram_user_id,
        "instagram_access_token": mask_key(settings.instagram_access_token),
        "threads_user_id": settings.threads_user_id,
        "threads_access_token": mask_key(settings.threads_access_token),
    }

@router.post("/")
def update_settings(data: dict):
    """Mock update settings (Thực tế cần lưu xuống file .env)"""
    return {"success": True, "message": "Settings saved successfully."}
