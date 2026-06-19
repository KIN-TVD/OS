import os
import base64
import uuid
from src.schemas.image import Image
from src.utils.logger import logger

def save_image(image: Image) -> str:
    """
    Lưu base64_data từ Image object ra file hệ thống.
    Trả về đường dẫn tĩnh.
    """
    if not image.base64_data:
        logger.error("No base64 data to save.")
        return ""

    logger.info("Saving image to disk...")

    storage_dir = "data/images"
    os.makedirs(storage_dir, exist_ok=True)
    
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(storage_dir, filename)

    try:
        image_data = base64.b64decode(image.base64_data)
        with open(filepath, "wb") as f:
            f.write(image_data)
            
        logger.info(f"Image saved successfully at {filepath}")
        image.url = f"/{filepath}" 
        return filepath
    except Exception as e:
        logger.error(f"Failed to save image: {e}")
        return ""
