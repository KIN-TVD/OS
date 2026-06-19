import json
import requests
from src.config.settings import settings
from src.schemas.angle import Angle
from src.schemas.caption import Caption
from src.utils.logger import logger

THREAD_SYSTEM_PROMPT = """Bạn là chuyên gia viết nội dung Threads (dạng X/Twitter) cho thị trường Việt Nam.
Viết 1 bài Threads dựa trên góc độ tiếp cận (angle) được cung cấp.

Yêu cầu:
- Tối đa 150 từ tiếng Việt
- Thẳng thắn, không vòng vo — đi thẳng vào insight chính ngay câu đầu
- Có thể dùng số thứ tự (1. 2. 3.) hoặc gạch đầu dòng để liệt kê
- Câu cuối là nhận định mạnh HOẶC câu hỏi kích thích thảo luận
- Không dùng emoji nhiều quá (tối đa 2-3 cái nếu có)

Trả về JSON hợp lệ:
{
  "id": "caption_threads",
  "platform": "threads",
  "text": "<nội dung bài Threads>"
}"""

def generate_thread(angle: Angle) -> Caption:
    """
    Tạo nội dung bài Threads ngắn gọn, súc tích từ Angle được chọn.
    """
    logger.info(f"Generating Threads post for angle: {angle.title}")

    user_message = f"Angle Title: {angle.title}\nAngle Description: {angle.description}"

    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": THREAD_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.75,
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
        thread = Caption(**raw)
        logger.info(f"Threads post generated ({len(thread.text)} chars)")
        return thread

    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Failed to parse thread response: {e}")
        return Caption(id="caption_threads", platform="threads", text="[Lỗi sinh nội dung Threads]")
    except requests.RequestException as e:
        logger.error(f"NVIDIA API call failed: {e}")
        return Caption(id="caption_threads", platform="threads", text="[API Error]")
