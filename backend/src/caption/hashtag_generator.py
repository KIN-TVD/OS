import json
import requests
from typing import List
from src.config.settings import settings
from src.utils.logger import logger

HASHTAG_SYSTEM_PROMPT = """Bạn là chuyên gia SEO và hashtag cho mạng xã hội Việt Nam.
Sinh ra danh sách 15 hashtag phù hợp dựa trên nội dung và chủ đề được cung cấp.

Yêu cầu:
- Mix hashtag tiếng Việt (60%) và tiếng Anh (40%)
- Bao gồm: 5 hashtag rộng (nhiều người follow), 5 hashtag trung bình, 5 hashtag niche/cụ thể
- Không có dấu cách trong hashtag, dùng camelCase hoặc liền nhau
- Mỗi hashtag bắt đầu bằng ký tự #

Trả về JSON hợp lệ:
{
  "hashtags": ["#hashtag1", "#hashtag2", ...]
}"""

def generate_hashtags(caption_text: str, topic: str) -> List[str]:
    """
    Sinh danh sách hashtag phù hợp dựa trên nội dung caption và chủ đề.
    """
    logger.info(f"Generating hashtags for topic: {topic}")

    user_message = f"Topic: {topic}\n\nCaption:\n{caption_text}"

    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": HASHTAG_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.6,
        "max_tokens": 512
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        raw = json.loads(content)
        hashtags = raw.get("hashtags", [])
        logger.info(f"Generated {len(hashtags)} hashtags")
        return hashtags

    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Failed to parse hashtag response: {e}")
        return []
    except requests.RequestException as e:
        logger.error(f"NVIDIA API call failed: {e}")
        return []
