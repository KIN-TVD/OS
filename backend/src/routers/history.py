import os
import glob
from fastapi import APIRouter
from src.storage.file_utils import DRAFTS_DIR, load_draft

router = APIRouter(prefix="/history", tags=["History"])

@router.get("/")
def get_history():
    pattern = os.path.join(DRAFTS_DIR, "*.json")
    files = glob.glob(pattern)
    
    history = []
    for f in files:
        draft_id = os.path.splitext(os.path.basename(f))[0]
        data = load_draft(draft_id)
        if not data: continue
        
        history.append({
            "id": draft_id,
            "title": data.get("title", "Untitled"),
            "status": data.get("status", "draft"),
            "platform": data.get("platform", "Unknown"),
            "created_at": data.get("created_at", ""),
            "has_image": bool(data.get("image") and data["image"].get("base64_data")),
            "score": data.get("caption_evaluation", {}).get("overall_score", 0) if data.get("caption_evaluation") else 0,
            "published_platforms": data.get("published_platforms", [])
        })
        
    history.sort(key=lambda x: x["created_at"], reverse=True)
    return history
