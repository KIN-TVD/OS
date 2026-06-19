import os
import glob
from fastapi import APIRouter, HTTPException
from src.storage.file_utils import OUTPUTS_DIR

router = APIRouter(prefix="/outputs", tags=["Outputs"])

@router.get("/")
def list_outputs():
    """Lấy danh sách các file Markdown đã xuất"""
    pattern = os.path.join(OUTPUTS_DIR, "*.md")
    files = sorted(glob.glob(pattern), key=os.path.getmtime, reverse=True)
    
    outputs = []
    for f in files:
        filename = os.path.basename(f)
        size = os.path.getsize(f)
        created_at = os.path.getctime(f)
        outputs.append({
            "filename": filename,
            "size": size,
            "created_at": created_at
        })
        
    return outputs

@router.get("/{filename}")
def get_output_content(filename: str):
    """Đọc nội dung của một file Markdown"""
    filepath = os.path.join(OUTPUTS_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    return {"filename": filename, "content": content}
