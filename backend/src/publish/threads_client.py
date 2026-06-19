import requests
from src.config.settings import settings
from src.utils.logger import logger

THREADS_API_BASE = "https://graph.threads.net/v1.0"


def publish_threads(text: str, image=None) -> dict:
    """
    Đăng bài lên Threads thông qua Meta Threads API (2-step: Container → Publish).

    Bước 1: Tạo media container kiểu TEXT hoặc IMAGE.
    Bước 2: Publish container.

    Yêu cầu:
    - THREADS_USER_ID trong .env
    - THREADS_ACCESS_TOKEN trong .env

    Returns:
        dict với keys: success, media_id hoặc error.
    """
    token = settings.threads_access_token
    user_id = settings.threads_user_id

    if not token or not user_id:
        logger.warning("Threads credentials not set. Returning mock response.")
        return {
            "success": False,
            "error": "THREADS_ACCESS_TOKEN hoặc THREADS_USER_ID chưa được cấu hình trong .env",
            "mock": True
        }

    logger.info(f"Publishing to Threads for user {user_id}...")

    # Step 1: Create media container
    create_url = f"{THREADS_API_BASE}/{user_id}/threads"
    
    # Truncate text to 500 characters (Threads limit)
    if len(text) > 500:
        logger.warning(f"Text is {len(text)} chars long. Truncating to 500 chars for Threads API.")
        text = text[:497] + "..."

    create_payload = {
        "text": text,
        "access_token": token,
    }

    if image and image.url and image.url.startswith("http"):
        create_payload["media_type"] = "IMAGE"
        # URL của ngrok hoặc domain public mới được Threads chấp nhận.
        create_payload["image_url"] = image.url
    else:
        create_payload["media_type"] = "TEXT"

    try:
        # Threads API thường yêu cầu truyền parameter qua query string (params) thay vì body (data)
        r = requests.post(create_url, params=create_payload, timeout=30)
        r.raise_for_status()
        container_id = r.json().get("id")
        logger.info(f"Threads container created: {container_id}")
    except requests.RequestException as e:
        err_msg = e.response.text if (e.response is not None and e.response.text) else str(e)
        logger.error(f"Failed to create Threads container: {err_msg}")
        return {"success": False, "error": f"Threads API Error: {err_msg}"}

    # Step 2: Publish container
    publish_url = f"{THREADS_API_BASE}/{user_id}/threads_publish"
    publish_payload = {
        "creation_id": container_id,
        "access_token": token,
    }

    try:
        r2 = requests.post(publish_url, params=publish_payload, timeout=30)
        r2.raise_for_status()
        media_id = r2.json().get("id")
        logger.info(f"Threads post published successfully. Media ID: {media_id}")
        return {"success": True, "media_id": media_id}
    except requests.RequestException as e:
        err_msg = e.response.text if (e.response is not None and e.response.text) else str(e)
        logger.error(f"Failed to publish Threads post: {err_msg}")
        return {"success": False, "error": f"Threads Publish Error: {err_msg}"}
