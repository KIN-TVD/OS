from typing import Dict, Any, List
from src.knowledge.dify_client import DifyClient
from src.utils.logger import logger

def search_dataset(query: str, dataset_id: str) -> List[Dict[str, Any]]:
    """
    Tìm kiếm thông tin từ một dataset cụ thể trên Dify.
    Sử dụng endpoint retrieve của Dify API.
    """
    logger.info(f"Searching dataset {dataset_id} for query: {query}")
    client = DifyClient()
    
    endpoint = f"datasets/{dataset_id}/retrieve"
    data = {
        "query": query,
        "retrieval_model": {
            "search_method": "hybrid",
            "reranking_enable": True,
            "top_k": 5
        }
    }
    
    response = client.post(endpoint, data)
    return response.get("records", [])

def retrieve_chunks(document_id: str) -> List[str]:
    """
    Lấy các chunks dữ liệu từ một tài liệu cụ thể.
    """
    logger.info(f"Retrieving chunks for document {document_id}")
    client = DifyClient()
    
    endpoint = f"documents/{document_id}/chunks"
    response = client.get(endpoint)
    
    chunks = response.get("data", [])
    return [chunk.get("content", "") for chunk in chunks if "content" in chunk]
