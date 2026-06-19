from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.storage.file_utils import load_draft, save_draft
from src.schemas.draft import Draft
from src.publish.instagram_client import publish_instagram
from src.publish.threads_client import publish_threads
from src.utils.logger import logger

router = APIRouter(prefix="/publish", tags=["Publish"])


class PublishRequest(BaseModel):
    draft_id: str


class PublishResponse(BaseModel):
    success: bool
    message: str
    media_id: str | None = None
    permalink: str | None = None
    mock: bool = False

@router.post("/{draft_id}", response_model=PublishResponse)
def publish_draft(draft_id: str, platform: str | None = None):
    """Publish draft lên MXH theo nền tảng được yêu cầu hoặc nền tảng mặc định trong draft."""
    data = load_draft(draft_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Draft '{draft_id}' not found")
    if data.get("status") not in ["approved", "published"]:
        raise HTTPException(status_code=400, detail="Draft phải được approve trước khi publish.")
    
    target_platform = platform if platform else data.get("platform", "instagram")
    draft = Draft(**data)
    
    if not draft.captions:
        raise HTTPException(status_code=400, detail="Draft không có caption.")
    
    # Ưu tiên caption phù hợp với target_platform
    caption_text = next(
        (c.text for c in draft.captions if c.platform == target_platform),
        draft.captions[0].text
    )
    
    if target_platform == "threads":
        result = publish_threads(caption_text, draft.image)
    else:
        # Default instagram
        result = publish_instagram(caption_text, draft.image)

    # Cập nhật trạng thái
    if result.get("success", False) or result.get("mock", False):
        data["status"] = "published"
        if "published_platforms" not in data:
            data["published_platforms"] = []
        if target_platform not in data["published_platforms"]:
            data["published_platforms"].append(target_platform)
        save_draft(draft_id, data)

    return PublishResponse(
        success=result.get("success", False),
        message=result.get("error", "Đăng thành công!") if not result.get("success") else f"Đã đăng bài lên {target_platform.capitalize()}!",
        media_id=result.get("media_id"),
        permalink=result.get("permalink"),
        mock=result.get("mock", False)
    )


@router.post("/instagram", response_model=PublishResponse)
def publish_to_instagram(body: PublishRequest):
    """
    Đăng bài lên Instagram từ Draft đã được approve.
    Yêu cầu Draft có status='approved' và image.url là URL công khai.
    """
    data = load_draft(body.draft_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Draft '{body.draft_id}' not found")

    if data.get("status") != "approved":
        raise HTTPException(status_code=400, detail="Draft phải được approve trước khi publish.")

    draft = Draft(**data)
    if not draft.captions:
        raise HTTPException(status_code=400, detail="Draft không có caption.")

    caption_text = draft.captions[0].text
    image = draft.image

    logger.info(f"Publishing draft '{body.draft_id}' to Instagram...")
    result = publish_instagram(caption_text, image)

    return PublishResponse(
        success=result.get("success", False),
        message=result.get("error", "Đăng thành công!") if not result.get("success") else "Đăng lên Instagram thành công!",
        media_id=result.get("media_id"),
        permalink=result.get("permalink"),
        mock=result.get("mock", False)
    )


@router.post("/threads", response_model=PublishResponse)
def publish_to_threads(body: PublishRequest):
    """
    Đăng bài lên Threads từ Draft đã được approve.
    """
    data = load_draft(body.draft_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Draft '{body.draft_id}' not found")

    if data.get("status") != "approved":
        raise HTTPException(status_code=400, detail="Draft phải được approve trước khi publish.")

    draft = Draft(**data)
    if not draft.captions:
        raise HTTPException(status_code=400, detail="Draft không có caption.")

    # Ưu tiên caption threads, fallback về instagram
    caption_text = next(
        (c.text for c in draft.captions if c.platform == "threads"),
        draft.captions[0].text
    )

    logger.info(f"Publishing draft '{body.draft_id}' to Threads...")
    result = publish_threads(caption_text)

    return PublishResponse(
        success=result.get("success", False),
        message=result.get("error", "Đăng thành công!") if not result.get("success") else "Đăng lên Threads thành công!",
        media_id=result.get("media_id"),
        mock=result.get("mock", False)
    )
