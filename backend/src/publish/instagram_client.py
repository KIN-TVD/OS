import requests
from src.config.settings import settings
from src.schemas.image import Image
from src.utils.logger import logger

GRAPH_API_BASE = "https://graph.facebook.com/v19.0"


def publish_instagram(caption: str, image: Image) -> dict:
    """
    Đăng bài lên Instagram thông qua Meta Graph API (2-step: Container → Publish).

    Bước 1: Tạo media container (image_url hoặc base64 CDN-hosted).
    Bước 2: Publish container.

    Yêu cầu:
    - INSTAGRAM_USER_ID trong .env
    - INSTAGRAM_ACCESS_TOKEN trong .env
    - image.url phải là URL công khai (CDN) hoặc bạn đã upload image lên CDN trước.

    Returns:
        dict với keys: success, media_id, permalink (nếu thành công) hoặc error.
    """
    token = settings.instagram_access_token
    user_id = settings.instagram_user_id

    if not token or not user_id:
        logger.warning("Instagram credentials not set. Returning mock response.")
        return {
            "success": False,
            "error": "INSTAGRAM_ACCESS_TOKEN hoặc INSTAGRAM_USER_ID chưa được cấu hình trong .env",
            "mock": True
        }

    image_url = image.url
    if not image_url or not image_url.startswith("http"):
        logger.error(f"Invalid image URL for Instagram: {image_url}")
        return {
            "success": False, 
            "error": "Instagram bắt buộc phải có link ảnh Public (https://...). Hiện tại bạn đang dùng link Local nội bộ."
        }

    logger.info(f"Publishing to Instagram for user {user_id}...")

    # Step 1: Create media container
    create_url = f"{GRAPH_API_BASE}/{user_id}/media"
    create_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": token,
    }

    try:
        r = requests.post(create_url, data=create_payload, timeout=30)
        r.raise_for_status()
        container_id = r.json().get("id")
        logger.info(f"Media container created: {container_id}")
    except requests.RequestException as e:
        err_msg = e.response.text if e.response else str(e)
        logger.error(f"Failed to create Instagram container: {err_msg}")
        return {"success": False, "error": err_msg}

    # Step 2: Publish container
    publish_url = f"{GRAPH_API_BASE}/{user_id}/media_publish"
    publish_payload = {
        "creation_id": container_id,
        "access_token": token,
    }

    try:
        r2 = requests.post(publish_url, data=publish_payload, timeout=30)
        r2.raise_for_status()
        media_id = r2.json().get("id")
        logger.info(f"Instagram post published successfully. Media ID: {media_id}")
        return {
            "success": True,
            "media_id": media_id,
            "permalink": f"https://www.instagram.com/p/{media_id}/"
        }
    except requests.RequestException as e:
        err_msg = e.response.text if e.response else str(e)
        logger.error(f"Failed to publish Instagram post: {err_msg}")
        return {"success": False, "error": err_msg}
