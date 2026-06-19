from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

from src.knowledge.dify_client import DifyClient
from src.knowledge.search import search_dataset, retrieve_chunks
from src.utils.logger import logger

router = APIRouter(prefix="/knowledge", tags=["Knowledge"])

class SearchRequest(BaseModel):
    query: str
    dataset_id: str

@router.get("/datasets")
def get_datasets():
    """Lấy danh sách Datasets từ Dify"""
    client = DifyClient()
    response = client.get("datasets")
    
    # Mock data if API key is invalid or not dataset API
    if not response or "data" not in response:
        logger.warning("Could not fetch datasets from Dify. Returning mock data.")
        return {
            "data": [
                {"id": "ds-1", "name": "General Knowledge", "document_count": 12, "word_count": 45000},
                {"id": "ds-2", "name": "AI & Technology", "document_count": 5, "word_count": 15000},
                {"id": "ds-3", "name": "Business", "document_count": 8, "word_count": 25000},
                {"id": "ds-4", "name": "Lifestyle", "document_count": 20, "word_count": 60000},
            ]
        }
    
    return response

@router.get("/datasets/{dataset_id}/documents")
def get_documents(dataset_id: str):
    """Lấy danh sách Documents trong một Dataset"""
    client = DifyClient()
    response = client.get(f"datasets/{dataset_id}/documents")
    
    if not response or "data" not in response:
        logger.warning(f"Could not fetch documents for dataset {dataset_id}. Returning mock data.")
        return {
            "data": [
                {"id": "doc-1", "name": "AI Trends 2025.pdf", "word_count": 5000, "status": "completed"},
                {"id": "doc-2", "name": "Content Marketing Strategy.md", "word_count": 3000, "status": "completed"},
                {"id": "doc-3", "name": "Brand Guidelines.docx", "word_count": 2000, "status": "processing"}
            ]
        }
        
    return response

@router.get("/documents/{document_id}/chunks")
def get_chunks(document_id: str):
    """Lấy danh sách Chunks của một Document"""
    chunks = retrieve_chunks(document_id)
    if not chunks:
        return {"data": [{"content": "Mock chunk 1: Trí tuệ nhân tạo đang thay đổi cách chúng ta sáng tạo nội dung."}, {"content": "Mock chunk 2: Tự động hóa quy trình giúp tiết kiệm 80% thời gian."}]}
    return {"data": [{"content": c} for c in chunks]}

@router.post("/search")
def search(request: SearchRequest):
    """Tìm kiếm nội dung trong Dataset (Hybrid Search)"""
    records = search_dataset(request.query, request.dataset_id)
    
    if not records:
        logger.warning("No records found or Dify API failed. Returning mock search results.")
        return {
            "records": [
                {"score": 0.92, "segment": {"content": f"Kết quả tìm kiếm giả lập cho: '{request.query}'. Đây là thông tin quan trọng được trích xuất từ Knowledge Base."}},
                {"score": 0.85, "segment": {"content": "Một kết quả khác liên quan đến chủ đề này. Các Agent AI có thể tự động đọc và phân tích đoạn văn bản này."}}
            ]
        }
        
    return {"records": records}
