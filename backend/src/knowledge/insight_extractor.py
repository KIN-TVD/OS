import requests
from typing import List
from src.config.settings import settings
from src.utils.logger import logger

def extract_insights(context_text: str) -> List[str]:
    """
    Trích xuất insights từ đoạn văn bản cho trước sử dụng OpenAI API.
    """
    logger.info("Extracting insights from context...")
    if not settings.nvidia_api_key:
        logger.warning("NVIDIA_API_KEY is not set. Returning mock insights.")
        return [
            "Mock Insight 1: Trí tuệ nhân tạo đang thay đổi cách tạo content.", 
            "Mock Insight 2: Nội dung cần ngắn gọn và súc tích."
        ]
        
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "meta/llama-3.1-70b-instruct",
        "messages": [
            {"role": "system", "content": "You are an expert content strategist. Extract 2-3 key insights from the following text. Return them as a bulleted list."},
            {"role": "user", "content": context_text}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        insights = [line.strip("- *").strip() for line in content.split("\n") if line.strip()]
        return insights
    except Exception as e:
        logger.error(f"Failed to extract insights: {e}")
        return []
