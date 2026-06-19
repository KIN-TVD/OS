import os
from typing import Dict, Any, Union
from src.storage.json_utils import save_json, load_json
from src.schemas.draft import Draft

# Định nghĩa các đường dẫn lưu trữ tĩnh (sẽ tạo thư mục data/ ở root của backend)
BASE_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
DRAFTS_DIR = os.path.join(BASE_DATA_DIR, "drafts")
IMAGES_DIR = os.path.join(BASE_DATA_DIR, "images")
LOGS_DIR = os.path.join(BASE_DATA_DIR, "logs")
OUTPUTS_DIR = os.path.join(BASE_DATA_DIR, "outputs")

# Đảm bảo các thư mục tồn tại khi module này được import
for directory in [DRAFTS_DIR, IMAGES_DIR, LOGS_DIR, OUTPUTS_DIR]:
    os.makedirs(directory, exist_ok=True)

def save_draft(draft_id: str, draft_data: Union[dict, Draft]) -> str:
    """
    Lưu thông tin bản thảo.
    Việc sử dụng function này làm interface giúp dễ dàng thay đổi logic 
    (ví dụ đổi từ lưu JSON sang Insert vào SQL Table) sau này mà không ảnh hưởng code bên ngoài.
    """
    if isinstance(draft_data, Draft):
        # Convert pydantic model to dict an toàn để lưu JSON
        data_to_save = draft_data.model_dump(mode='json')
    else:
        data_to_save = draft_data

    filepath = os.path.join(DRAFTS_DIR, f"{draft_id}.json")
    save_json(filepath, data_to_save)
    return filepath

def load_draft(draft_id: str) -> Dict[str, Any]:
    """
    Tải thông tin bản thảo.
    Sau này sẽ đổi thành truy vấn SELECT từ Database.
    """
    filepath = os.path.join(DRAFTS_DIR, f"{draft_id}.json")
    return load_json(filepath)
