import os
import glob
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

from src.storage.file_utils import DRAFTS_DIR, load_draft
from src.utils.logger import logger

router = APIRouter(prefix="/missions", tags=["Missions"])


class Mission(BaseModel):
    id: str
    title: str
    status: str
    created_at: str
    caption_score: float | None = None
    image_score: float | None = None
    progress: int  # 0-100


def _draft_to_mission(data: dict) -> Mission:
    """Chuyển Draft JSON thành Mission summary."""
    cap_eval = data.get("caption_evaluation")
    img_eval = data.get("image_evaluation")
    cap_score = cap_eval.get("overall_score") if cap_eval else None
    img_score = img_eval.get("overall_score") if img_eval else None

    # Tính progress dựa trên dữ liệu có sẵn
    steps_done = 0
    if data.get("angle"): steps_done += 20
    if data.get("captions"): steps_done += 20
    if cap_eval: steps_done += 20
    if data.get("image"): steps_done += 20
    if img_eval: steps_done += 20

    return Mission(
        id=data.get("id", ""),
        title=data.get("title", ""),
        status=data.get("status", "pending"),
        created_at=str(data.get("created_at", "")),
        caption_score=cap_score,
        image_score=img_score,
        progress=steps_done
    )


@router.get("/", response_model=List[Mission])
def list_missions():
    """Trả về danh sách tất cả missions (từ drafts)."""
    pattern = os.path.join(DRAFTS_DIR, "*.json")
    files = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)

    missions = []
    for f in files:
        draft_id = os.path.splitext(os.path.basename(f))[0]
        data = load_draft(draft_id)
        if data:
            missions.append(_draft_to_mission(data))
    return missions
