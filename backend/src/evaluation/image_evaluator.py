import json
import requests
from src.config.settings import settings
from src.schemas.image import Image
from src.schemas.evaluation import ImageEvaluation
from src.utils.logger import logger

IMAGE_EVAL_PROMPT = """Bạn là chuyên gia đánh giá chất lượng hình ảnh (AI Image Quality Assessor).
Hãy đánh giá hình ảnh được cung cấp dựa trên 4 tiêu chí sau:
1. Character: Nhân vật/chủ thể có rõ ràng, chi tiết và không bị biến dạng không?
2. Composition: Bố cục hình ảnh có hài hòa, tập trung vào chủ thể chính không?
3. Color: Màu sắc có đẹp, ăn nhập với nhau và đúng ánh sáng không?
4. Style: Phong cách nghệ thuật có đồng nhất không?

Yêu cầu:
- Chấm điểm từng tiêu chí từ 1 đến 10.
- Tính điểm trung bình (overall_score).
- Nhận xét ngắn gọn (comments) về điểm mạnh và điểm yếu.

Trả về ONLY một JSON hợp lệ:
{
  "character_score": <float>,
  "composition_score": <float>,
  "color_score": <float>,
  "style_score": <float>,
  "overall_score": <float>,
  "comments": "<nhận xét>"
}"""

def evaluate_image(image: Image) -> ImageEvaluation:
    """
    Đánh giá chất lượng ảnh dùng NVIDIA API (meta/llama-3.2-90b-vision-instruct).
    """
    logger.info("Evaluating image quality...")

    if not settings.nvidia_api_key or not image.base64_data:
        logger.warning("Missing API key or image data. Returning mock evaluation.")
        return ImageEvaluation(
            character_score=8.0, composition_score=8.0, color_score=8.0, 
            style_score=8.0, overall_score=8.0, comments="Mock pass."
        )

    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    
    img_data = image.base64_data
    if not img_data.startswith("data:image"):
        img_data = f"data:image/png;base64,{img_data}"

    payload = {
        "model": "meta/llama-3.2-90b-vision-instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": IMAGE_EVAL_PROMPT},
                    {"type": "image_url", "image_url": {"url": img_data}}
                ]
            }
        ],
        "temperature": 0.3,
        "max_tokens": 1024
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        elif "{" in content and "}" in content:
            # Fallback parse the JSON object out of random text
            start = content.find("{")
            end = content.rfind("}") + 1
            content = content[start:end]

        raw = json.loads(content)
        evaluation = ImageEvaluation(**raw)
        logger.info(f"Image evaluation result: {evaluation.overall_score}")
        return evaluation
    except Exception as e:
        logger.error(f"Image evaluation failed: {e}")
        return ImageEvaluation(character_score=0, composition_score=0, color_score=0, style_score=0, overall_score=0, comments=f"Error: {str(e)}")
