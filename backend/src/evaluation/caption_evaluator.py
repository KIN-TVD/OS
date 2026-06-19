import json
import requests
from src.config.settings import settings
from src.schemas.caption import Caption
from src.schemas.evaluation import CaptionEvaluation
from src.utils.logger import logger

EVALUATION_SYSTEM_PROMPT = """Bạn là một chuyên gia đánh giá chất lượng nội dung mạng xã hội (Content Quality Assessor).
Đánh giá đoạn caption được cung cấp dựa trên 5 tiêu chí sau đây:
1. Hook: Câu mở đầu có đủ hấp dẫn và gây tò mò không?
2. Emotion: Bài viết có chạm đến cảm xúc người đọc không?
3. Insight: Có chứa sự thật ngầm hiểu sâu sắc không?
4. CTA: Lời kêu gọi hành động có rõ ràng và thuyết phục không?
5. Clarity: Văn phong có rõ ràng, dễ hiểu, không rườm rà không?

Yêu cầu:
- Chấm điểm từng tiêu chí từ 1 đến 10.
- Tính điểm trung bình (overall_score).
- Đưa ra feedback ngắn gọn (dưới 3 câu) về những điểm cần cải thiện vào biến comments.

Trả về ONLY một JSON hợp lệ có định dạng:
{
  "hook_score": <float>,
  "emotion_score": <float>,
  "insight_score": <float>,
  "cta_score": <float>,
  "clarity_score": <float>,
  "overall_score": <float>,
  "comments": "<nhận xét>"
}"""

def evaluate_caption(caption: Caption) -> CaptionEvaluation:
    """
    Đánh giá chất lượng caption thông qua NVIDIA API.
    """
    logger.info(f"Evaluating caption for platform: {caption.platform}")

    if not settings.nvidia_api_key:
        logger.warning("NVIDIA_API_KEY is not set. Returning mock evaluation.")
        return CaptionEvaluation(
            hook_score=8.5, emotion_score=8.5, insight_score=8.5, 
            cta_score=8.5, clarity_score=8.5, overall_score=8.5, 
            comments="Mock feedback: Rất tốt."
        )

    user_message = f"Platform: {caption.platform}\nCaption Text:\n{caption.text}"
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": EVALUATION_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.3,
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
        evaluation = CaptionEvaluation(**raw)
        logger.info(f"Evaluation result: Score {evaluation.overall_score}")
        return evaluation

    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Failed to parse evaluation response: {e}")
        return CaptionEvaluation(hook_score=0.0, emotion_score=0.0, insight_score=0.0, cta_score=0.0, clarity_score=0.0, overall_score=0.0, comments="JSON Parse Error")
    except requests.RequestException as e:
        logger.error(f"NVIDIA API call failed: {e}")
        return CaptionEvaluation(hook_score=0.0, emotion_score=0.0, insight_score=0.0, cta_score=0.0, clarity_score=0.0, overall_score=0.0, comments="API Request Error")
