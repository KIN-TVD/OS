import os
import glob
from fastapi import APIRouter
from src.storage.file_utils import DRAFTS_DIR, load_draft

router = APIRouter(prefix="/evaluations", tags=["Evaluations"])

@router.get("/")
def get_evaluations_summary():
    """Thống kê điểm số đánh giá từ tất cả bản thảo"""
    pattern = os.path.join(DRAFTS_DIR, "*.json")
    files = glob.glob(pattern)
    
    total_drafts = 0
    cap_stats = {"hook": 0, "emotion": 0, "insight": 0, "cta": 0, "clarity": 0, "overall": 0}
    img_stats = {"character": 0, "composition": 0, "color": 0, "style": 0, "overall": 0}
    cap_count = 0
    img_count = 0
    
    history = []
    
    for f in files:
        draft_id = os.path.splitext(os.path.basename(f))[0]
        data = load_draft(draft_id)
        if not data: continue
        
        total_drafts += 1
        created_at = data.get("created_at", "")
        title = data.get("title", "")
        
        history_item = {
            "id": draft_id,
            "title": title,
            "created_at": created_at,
            "caption_score": 0,
            "image_score": 0
        }
        
        # Caption eval
        ce = data.get("caption_evaluation")
        if ce:
            cap_count += 1
            cap_stats["hook"] += ce.get("hook_score", 0)
            cap_stats["emotion"] += ce.get("emotion_score", 0)
            cap_stats["insight"] += ce.get("insight_score", 0)
            cap_stats["cta"] += ce.get("cta_score", 0)
            cap_stats["clarity"] += ce.get("clarity_score", 0)
            cap_stats["overall"] += ce.get("overall_score", 0)
            history_item["caption_score"] = ce.get("overall_score", 0)
            
        # Image eval
        ie = data.get("image_evaluation")
        if ie:
            img_count += 1
            img_stats["character"] += ie.get("character_score", 0)
            img_stats["composition"] += ie.get("composition_score", 0)
            img_stats["color"] += ie.get("color_score", 0)
            img_stats["style"] += ie.get("style_score", 0)
            img_stats["overall"] += ie.get("overall_score", 0)
            history_item["image_score"] = ie.get("overall_score", 0)
            
        history.append(history_item)
        
    # Calculate averages
    avg_cap = {k: round(v / cap_count, 1) if cap_count > 0 else 0 for k, v in cap_stats.items()}
    avg_img = {k: round(v / img_count, 1) if img_count > 0 else 0 for k, v in img_stats.items()}
    
    history.sort(key=lambda x: x["created_at"])
    
    return {
        "total_drafts": total_drafts,
        "caption_averages": avg_cap,
        "image_averages": avg_img,
        "history": history
    }
