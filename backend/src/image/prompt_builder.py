import json
import requests
from src.config.settings import settings
from src.schemas.caption import Caption
from src.utils.logger import logger

PROMPT_BUILDER_SYSTEM = """You are an expert AI image prompt engineer.
Analyze the provided Vietnamese caption and generate a highly detailed, descriptive image generation prompt in English.
The prompt should be optimized for advanced text-to-image models like Flux or Midjourney.

Requirements for the prompt:
- Describe the main subject clearly.
- Specify the composition and setting.
- Specify the lighting (e.g., cinematic lighting, soft natural light).
- Specify the style (e.g., highly detailed photography, anime style, flat illustration).
- Do NOT include any text/words in the image prompt unless absolutely necessary.

Return ONLY a valid JSON:
{
  "prompt": "<your english image prompt here>"
}

WARNING: The "prompt" value MUST BE TRANSLATED TO STRICTLY ENGLISH. Do not use Vietnamese."""

def build_prompt(caption: Caption) -> str:
    """
    Sinh prompt tiếng Anh cho model sinh ảnh dựa trên nội dung caption.
    """
    logger.info("Building image prompt from caption.")

    if not settings.nvidia_api_key:
        logger.warning("NVIDIA_API_KEY is not set. Returning mock prompt.")
        return "A cinematic shot of a glowing AI brain, highly detailed, cyberpunk aesthetic, neon lights"

    user_message = f"Caption:\n{caption.text}"
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": PROMPT_BUILDER_SYSTEM},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=8)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()

        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        raw = json.loads(content)
        prompt = raw.get("prompt", "")
        logger.info(f"Built prompt: {prompt}")
        return prompt

    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Failed to parse prompt response: {e}")
        return "A beautiful generic placeholder image, highly detailed"
    except requests.RequestException as e:
        logger.error(f"NVIDIA API call failed: {e}")
        return "A beautiful generic placeholder image, highly detailed"
