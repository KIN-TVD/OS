import json
import requests
from typing import List
from src.config.settings import settings
from src.schemas.angle import Angle
from src.utils.logger import logger

SYSTEM_PROMPT = """You are a senior content strategist specializing in social media for Vietnamese audiences.

Given a topic and a list of key insights, generate exactly 3 creative content angles.
Each angle must be distinct — covering different emotional tones or content styles:
  - One should be emotion-driven (story, empathy, relatability)
  - One should be educational or data-driven (tips, facts, how-to)
  - One should be action/results-oriented (case study, transformation, call to action)

Return ONLY a valid JSON array (no markdown, no explanation) in this exact format:
[
  {
    "id": "angle_1",
    "title": "<short catchy title>",
    "description": "<2-3 sentence description of the angle approach>",
    "confidence_score": <float between 0.0 and 1.0>
  },
  ...
]"""

def generate_angles(insights: List[str], topic: str) -> List[Angle]:
    """
    Tạo ra 3 góc độ tiếp cận nội dung dựa trên topic và insights.
    Gọi NVIDIA API để sinh nội dung.
    """
    logger.info(f"Generating angles for topic: {topic}")

    if not settings.nvidia_api_key:
        logger.warning("NVIDIA_API_KEY is not set. Returning mock angles.")
        return [
            Angle(id="angle_1", title="Góc Cảm Xúc (Mock)", description="Kể câu chuyện thực từ người dùng để tạo sự đồng cảm.", confidence_score=0.85),
            Angle(id="angle_2", title="Góc Giáo Dục (Mock)", description="Chia sẻ 3 sự thật ít ai biết về chủ đề này.", confidence_score=0.80),
            Angle(id="angle_3", title="Góc Kết Quả (Mock)", description="Trình bày case study thực tế và kết quả đo lường được.", confidence_score=0.78),
        ]

    insights_text = "\n".join(f"- {i}" for i in insights)
    user_message = f"Topic: {topic}\n\nKey Insights:\n{insights_text}"

    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.8,
        "max_tokens": 1024
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=8)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        # Extract JSON from response (in case of markdown code block)
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        elif "[" in content and "]" in content:
            start = content.find("[")
            end = content.rfind("]") + 1
            content = content[start:end]

        raw_angles = json.loads(content)
        angles = [Angle(**a) for a in raw_angles]
        logger.info(f"Generated {len(angles)} angles successfully.")
        return angles
    except Exception as e:
        logger.error(f"Angle generation failed: {e}. Falling back to topic-specific mock angles.")
        return [
            Angle(id="angle_1", title=f"Góc Nhìn Cảm Xúc: Sự đồng cảm về {topic}", description=f"Kể một câu chuyện thực tế về cách {topic} giúp giải quyết các vấn đề thường nhật và tạo sự kết nối chân thành.", confidence_score=0.88),
            Angle(id="angle_2", title=f"Góc Nhìn Giáo Dục: Khám phá tri thức {topic}", description=f"Cung cấp 3 thông tin bổ ích và giá trị khoa học cốt lõi liên quan đến {topic} mà người đọc chưa biết.", confidence_score=0.82),
            Angle(id="angle_3", title=f"Góc Nhìn Thực Tế: Ứng dụng {topic} hiệu quả", description=f"Trình bày phương pháp thực chiến và các bước cụ thể để ứng dụng {topic} nâng cao năng suất mỗi ngày.", confidence_score=0.79),
        ]

def select_best_angle(angles: List[Angle]) -> Angle:
    if not angles:
        return None
    return max(angles, key=lambda a: a.confidence_score)
