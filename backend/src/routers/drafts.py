import os
import glob
from typing import List
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel

from src.schemas.draft import Draft
from src.storage.file_utils import DRAFTS_DIR, load_draft, save_draft
from src.storage.json_utils import save_json
from src.publish import export_markdown
from src.utils.logger import logger

router = APIRouter(prefix="/drafts", tags=["Drafts"])


# ──────────────────────────────────────────
# Response models
# ──────────────────────────────────────────

class DraftSummary(BaseModel):
    id: str
    title: str
    status: str
    created_at: str

class ActionResponse(BaseModel):
    success: bool
    message: str
    draft_id: str


# ──────────────────────────────────────────
# GET /drafts  — Lấy danh sách tất cả bản nháp
# ──────────────────────────────────────────

@router.get("/", response_model=List[DraftSummary])
def list_drafts():
    """Trả về danh sách tất cả bản nháp đã tạo (summary)."""
    pattern = os.path.join(DRAFTS_DIR, "*.json")
    files = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)

    summaries = []
    for f in files:
        data = load_draft(os.path.splitext(os.path.basename(f))[0])
        if data:
            summaries.append(DraftSummary(
                id=data.get("id", ""),
                title=data.get("title", ""),
                status=data.get("status", "pending"),
                created_at=str(data.get("created_at", ""))
            ))
    return summaries


# ──────────────────────────────────────────
# GET /drafts/{draft_id}  — Lấy chi tiết bản nháp
# ──────────────────────────────────────────

@router.get("/{draft_id}")
def get_draft(draft_id: str):
    """Trả về chi tiết đầy đủ của một bản nháp."""
    data = load_draft(draft_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Draft '{draft_id}' not found")
    return data

@router.put("/{draft_id}")
def update_draft(draft_id: str, payload: dict):
    """Cập nhật dữ liệu cho bản nháp."""
    data = load_draft(draft_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Draft '{draft_id}' not found")
    
    # Update captions if provided
    if "captions" in payload:
        data["captions"] = payload["captions"]
        
    # Update image if provided
    if "image" in payload:
        if "image" not in data or not data["image"]:
            data["image"] = payload["image"]
        else:
            data["image"].update(payload["image"])
            
    # Export markdown if approved
    if data.get("status") == "approved":
        try:
            draft_obj = Draft(**data)
            export_markdown(draft_obj)
        except Exception as e:
            logger.error(f"Re-export markdown failed: {e}")

    save_draft(draft_id, data)
    return {"success": True, "message": "Draft updated"}


# ──────────────────────────────────────────
# POST /drafts/{draft_id}/approve
# ──────────────────────────────────────────

@router.post("/{draft_id}/approve", response_model=ActionResponse)
def approve_draft(draft_id: str):
    """Duyệt bản nháp — đổi status thành 'approved' và export Markdown."""
    data = load_draft(draft_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Draft '{draft_id}' not found")

    data["status"] = "approved"
    save_draft(draft_id, data)

    # Export sang Markdown
    try:
        draft_obj = Draft(**data)
        md_path = export_markdown(draft_obj)
        logger.info(f"Draft '{draft_id}' approved. Markdown: {md_path}")
        return ActionResponse(success=True, message=f"Draft approved. Markdown at {md_path}", draft_id=draft_id)
    except Exception as e:
        logger.error(f"Approve export failed: {e}")
        return ActionResponse(success=True, message="Approved but Markdown export failed.", draft_id=draft_id)


# ──────────────────────────────────────────
# POST /drafts/{draft_id}/reject
# ──────────────────────────────────────────

@router.post("/{draft_id}/reject", response_model=ActionResponse)
def reject_draft(draft_id: str):
    """Từ chối bản nháp — đổi status thành 'rejected'."""
    data = load_draft(draft_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Draft '{draft_id}' not found")

    data["status"] = "rejected"
    save_draft(draft_id, data)
    logger.info(f"Draft '{draft_id}' rejected.")
    return ActionResponse(success=True, message="Draft rejected.", draft_id=draft_id)


# ──────────────────────────────────────────
# POST /drafts/rerun  — Chạy lại pipeline tạo Draft mới
# ──────────────────────────────────────────

class RerunRequest(BaseModel):
    topic: str
    platform: str = "instagram"

def _run_pipeline_bg(topic: str, platform: str):
    from src.pipeline import run_pipeline
    try:
        run_pipeline(topic, platform)
    except Exception as e:
        logger.error(f"Background pipeline failed: {e}")

@router.post("/rerun", response_model=ActionResponse)
def rerun_pipeline(body: RerunRequest, background_tasks: BackgroundTasks):
    """Kích hoạt pipeline ngầm để tạo một bản nháp mới từ chủ đề cho trước."""
    try:
        logger.info(f"Rerun pipeline (Background): topic='{body.topic}', platform='{body.platform}'")
        background_tasks.add_task(_run_pipeline_bg, body.topic, body.platform)
        return ActionResponse(
            success=True,
            message="Pipeline đang chạy ngầm. Vui lòng kiểm tra mục Nhiệm vụ (Missions).",
            draft_id="processing"
        )
    except Exception as e:
        logger.error(f"Pipeline start failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
