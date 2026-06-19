import requests
import json
from src.schemas.image import Image
from src.schemas.evaluation import ImageEvaluation
from src.image.image_generator import generate_image
from src.config.settings import settings
from src.utils.logger import logger

RETRY_IMAGE_PROMPT = """Bạn là chuyên gia viết Image Prompt cho AI (Flux/Midjourney).
Hình ảnh trước đó sinh ra từ prompt gốc không đạt yêu cầu.
Dưới đây là prompt cũ và nhận xét (feedback) của giám khảo.

Nhiệm vụ: Viết lại một Prompt tiếng Anh mới hoàn toàn, khắc phục các nhược điểm trong feedback (VD: lỗi bố cục, lỗi màu sắc, chủ thể không rõ ràng). 

Trả về ONLY một JSON hợp lệ:
{
  "new_prompt": "<english prompt>"
}"""

def improve_image(image: Image, evaluation: ImageEvaluation) -> Image:
    """
    Nếu ảnh không đạt, viết lại prompt dựa trên feedback và sinh lại ảnh mới.
    """
    if evaluation.overall_score >= 8.0:
        logger.info("Image already passed. No improvement needed.")
        return image

    logger.info(f"Improving image prompt based on feedback: {evaluation.comments}")

    if not settings.nvidia_api_key:
        logger.warning("No API key. Returning original image.")
        return image

    user_message = f"Original Prompt: {image.prompt}\nFeedback: {evaluation.comments}"
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": RETRY_IMAGE_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        raw = json.loads(content)
        new_prompt = raw.get("new_prompt", image.prompt)
        logger.info(f"Generated improved prompt: {new_prompt}")
        
        # Gọi sinh lại ảnh từ prompt mới
        return generate_image(new_prompt)
        
    except Exception as e:
        logger.error(f"Failed to improve image: {e}")
        return image
