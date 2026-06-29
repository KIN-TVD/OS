import json
import requests
from src.config.settings import settings
from src.schemas.angle import Angle
from src.schemas.caption import Caption
from src.utils.logger import logger

INSTAGRAM_SYSTEM_PROMPT = """Bạn là chuyên gia viết nội dung Instagram cho thị trường Việt Nam.
Viết 1 caption Instagram dựa trên góc độ tiếp cận (angle) được cung cấp.

Yêu cầu:
- Dài 150-250 từ (tiếng Việt)
- Mở đầu bằng 1-2 câu Hook mạnh, gây tò mò hoặc cộng hưởng cảm xúc
- Thân bài trình bày nội dung theo angle được chọn
- Kết thúc bằng CTA (Call To Action) rõ ràng
- Giọng văn gần gũi, chân thật, phù hợp mạng xã hội

Trả về JSON hợp lệ theo định dạng:
{
  "id": "caption_instagram",
  "platform": "instagram",
  "text": "<nội dung caption>"
}"""

THREADS_SYSTEM_PROMPT = """Bạn là chuyên gia viết nội dung Threads cho thị trường Việt Nam.
Viết 1 caption Threads dựa trên góc độ tiếp cận (angle) được cung cấp.

Yêu cầu:
- Tuyệt đối ngắn gọn, tổng độ dài KHÔNG ĐƯỢC VƯỢT QUÁ 500 KÝ TỰ.
- Thẳng thắn, súc tích, đi thẳng vào vấn đề — không giải thích dài dòng
- Dạng text-based: có thể dùng số đầu dòng hoặc bullet points
- Kết thúc bằng 1 câu hỏi mở hoặc nhận định mạnh

Trả về JSON hợp lệ theo định dạng:
{
  "id": "caption_threads",
  "platform": "threads",
  "text": "<nội dung caption>"
}"""

def generate_caption(angle: Angle, platform: str = "instagram") -> Caption:
    """
    Tạo caption cho nền tảng cụ thể dựa trên Angle đã chọn.
    platform: 'instagram' hoặc 'threads'
    """
    logger.info(f"Generating caption for {platform} with angle: {angle.title}")

    system_prompt = INSTAGRAM_SYSTEM_PROMPT if platform == "instagram" else THREADS_SYSTEM_PROMPT
    user_message = f"Angle Title: {angle.title}\nAngle Description: {angle.description}"

    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.85,
        "max_tokens": 1024
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=8)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        # Extract JSON từ response (đề phòng có markdown fence)
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        raw = json.loads(content)
        caption = Caption(**raw)
        logger.info(f"Caption generated for {platform} ({len(caption.text)} chars)")
        return caption
    except Exception as e:
        logger.error(f"Caption generation failed: {e}. Falling back to topic-specific mock caption.")
        text = (
            f"🚀 [GỢI Ý] Nâng tầm hiệu suất cùng: {angle.title}!\n\n"
            f"Bạn có biết rằng {angle.description.lower().replace('.', '')}?\n\n"
            f"Được thiết kế tinh tế và tối ưu cho các chuyên gia tốc độ cao, Apollo là sự giao thoa hoàn hảo giữa "
            f"thẩm mỹ tối giản và công năng vượt trội. Đừng để không gian làm việc của bạn bị giới hạn. 🌟\n\n"
            f"👉 Nhấp vào liên kết ở phần tiểu sử để đặt mua ngay hôm nay hoặc tìm hiểu thêm thông tin chi tiết!\n\n"
            f"#ApolloSeries #AgentOS #Workspace #Minimalism"
        )
        return Caption(id=f"caption_{platform}", platform=platform, text=text)
