import os
import glob
from fastapi import APIRouter
from src.storage.file_utils import DRAFTS_DIR, load_draft
from collections import defaultdict
from datetime import datetime

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary")
def get_dashboard_summary():
    pattern = os.path.join(DRAFTS_DIR, "*.json")
    files = glob.glob(pattern)
    
    total_drafts = len(files)
    published_count = 0
    total_score = 0
    scored_drafts = 0
    
    # Trends by date (YYYY-MM-DD)
    content_trend = defaultdict(int)
    eval_trend = defaultdict(list)
    generation_trend = defaultdict(int)

    for f in files:
        draft_id = os.path.splitext(os.path.basename(f))[0]
        data = load_draft(draft_id)
        if not data: continue
        
        status = data.get("status", "draft")
        if status == "approved":
            published_count += 1
            
        # Parse date
        created_at_str = data.get("created_at", "")
        if created_at_str:
            try:
                # "2026-06-16 08:31:00" -> "06/16"
                dt = datetime.strptime(created_at_str.split(".")[0][:19], "%Y-%m-%d %H:%M:%S")
                date_key = dt.strftime("%m/%d")
            except:
                date_key = "Unknown"
        else:
            date_key = "Unknown"
            
        content_trend[date_key] += 1
        
        has_image = bool(data.get("image") and data["image"].get("base64_data"))
        if has_image:
            generation_trend[date_key] += 1
        
        ce = data.get("caption_evaluation")
        if ce:
            score = ce.get("overall_score", 0)
            total_score += score
            scored_drafts += 1
            eval_trend[date_key].append(score)

    success_rate = (published_count / total_drafts * 100) if total_drafts > 0 else 0
    avg_score = (total_score / scored_drafts) if scored_drafts > 0 else 0
    
    # Format charts data
    chart_data = []
    dates = sorted(list(content_trend.keys()))
    if "Unknown" in dates: dates.remove("Unknown")
    
    for d in dates[-7:]: # last 7 days
        avg_eval_day = sum(eval_trend[d])/len(eval_trend[d]) if eval_trend[d] else 0
        chart_data.append({
            "name": d,
            "Drafts": content_trend[d],
            "Images": generation_trend[d],
            "Score": round(avg_eval_day, 1)
        })

    return {
        "summary": {
            "draft_count": total_drafts,
            "published_count": published_count,
            "success_rate": round(success_rate, 1),
            "average_score": round(avg_score, 1)
        },
        "trends": chart_data
    }
