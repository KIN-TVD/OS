import json
import requests
from typing import List
from src.config.settings import settings
from src.schemas.angle import Angle
from src.utils.logger import logger

SELECTOR_PROMPT = """You are a content performance analyst for social media.

Given a list of content angles, evaluate each one and select the SINGLE BEST angle based on the given criteria.
Return ONLY a valid JSON object (no markdown, no explanation) with the id of the best angle:
{
  "selected_id": "<id of the best angle>",
  "reasoning": "<1 sentence explanation>"
}"""

def select_best_angle(angles: List[Angle], criteria: str = "engagement") -> Angle:
    """
    Chọn góc độ tốt nhất trong danh sách angles dựa trên tiêu chí.
    Mặc định tiêu chí là engagement (tỉ lệ tương tác).
    """
    if not angles:
        raise ValueError("Danh sách angles không được rỗng.")

    if len(angles) == 1:
        return angles[0]

    logger.info(f"Selecting best angle from {len(angles)} angles. Criteria: {criteria}")

    if not settings.nvidia_api_key:
        logger.warning("NVIDIA_API_KEY is not set. Selecting first angle as default.")
        # Trả về angle có confidence_score cao nhất
        return max(angles, key=lambda a: a.confidence_score or 0)

    angles_json = json.dumps(
        [{"id": a.id, "title": a.title, "description": a.description} for a in angles],
        ensure_ascii=False, indent=2
    )
    user_message = f"Selection Criteria: {criteria}\n\nAngles to evaluate:\n{angles_json}"

    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": SELECTOR_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.3,
        "max_tokens": 256
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        result = json.loads(content)
        selected_id = result.get("selected_id")
        reasoning = result.get("reasoning", "")

        # Tìm angle tương ứng trong danh sách
        selected = next((a for a in angles if a.id == selected_id), angles[0])
        logger.info(f"Selected angle: '{selected.title}'. Reasoning: {reasoning}")
        return selected
    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Failed to parse selector response: {e}. Falling back to highest confidence.")
        return max(angles, key=lambda a: a.confidence_score or 0)
    except requests.RequestException as e:
        logger.error(f"NVIDIA API call failed: {e}. Falling back to highest confidence.")
        return max(angles, key=lambda a: a.confidence_score or 0)
