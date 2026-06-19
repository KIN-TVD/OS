import json
import requests
from src.config.settings import settings
from src.schemas.caption import Caption
from src.schemas.evaluation import CaptionEvaluation
from src.utils.logger import logger

RETRY_SYSTEM_PROMPT = """Bạn là chuyên gia biên tập nội dung.
Nhiệm vụ của bạn là sửa và cải thiện một đoạn caption bị đánh giá thấp dựa trên phản hồi (feedback) của giám khảo.

Yêu cầu:
- GIỮ NGUYÊN văn phong và những phần đã viết tốt.
- CHỈ SỬA những lỗi hoặc điểm yếu được nhắc đến trong feedback (VD: thêm Hook, sửa CTA).
- Trả về nội dung caption mới sau khi đã được tối ưu.

Trả về ONLY một JSON hợp lệ:
{
  "text": "<nội dung caption đã sửa>"
}"""

def improve_caption(caption: Caption, evaluation: CaptionEvaluation) -> Caption:
    """
    Cải thiện caption nếu chưa pass evaluation.
    """
    if evaluation.overall_score >= 8.0:
        logger.info("Caption already passed. No improvement needed.")
        return caption

    logger.info(f"Improving caption. Feedback: {evaluation.comments}")

    if not settings.nvidia_api_key:
        logger.warning("NVIDIA_API_KEY is not set. Returning unmodified caption.")
        return caption

    user_message = f"Original Caption:\n{caption.text}\n\nFeedback to fix:\n{evaluation.comments}"
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": RETRY_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.6,
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

        raw = json.loads(content)
        new_text = raw.get("text", caption.text)
        
        improved_caption = Caption(
            id=caption.id,
            platform=caption.platform,
            text=new_text
        )
        logger.info("Successfully improved caption.")
        return improved_caption

    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Failed to parse retry response: {e}")
        return caption
    except requests.RequestException as e:
        logger.error(f"NVIDIA API call failed during retry: {e}")
        return caption
