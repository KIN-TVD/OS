import requests
from src.config.settings import settings
from src.schemas.image import Image
from src.utils.logger import logger

def generate_image(prompt: str) -> Image:
    """
    Gọi Gemini API (Imagen 3) để sinh ảnh từ prompt qua OpenAI-compatible endpoint.
    Trả về đối tượng Image (chứa base64 data).
    """
    logger.info("Generating image via Gemini API...")

    if not settings.gemini_api_key:
        logger.warning("GEMINI_API_KEY is not set. Returning mock image.")
        return Image(id="img_mock", prompt=prompt, url="", base64_data="mock_base64_string", format="png")

    url = "https://generativelanguage.googleapis.com/v1beta/openai/images/generations"
    headers = {
        "Authorization": f"Bearer {settings.gemini_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "imagen-3.0-generate-002",
        "prompt": prompt,
        "response_format": "b64_json",
        "n": 1
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()
        
        b64_data = result["data"][0]["b64_json"]
        logger.info("Image generated successfully via Gemini API.")
        
        return Image(
            id="img_generated",
            prompt=prompt,
            url="",  
            base64_data=b64_data,
            format="png"
        )
    except Exception as e:
        logger.error(f"Gemini Image Generation failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
             logger.error(f"Response: {e.response.text}")
        return Image(id="img_error", prompt=prompt, url="", base64_data="", format="png")
