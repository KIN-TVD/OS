# Sprint 4 Report

## Objective
Tạo Knowledge Module (Module Xử lý Tri thức) chịu trách nhiệm giao tiếp với nguồn dữ liệu (Dify API) và trích xuất sự thật ngầm hiểu - Insights (OpenAI API).

## Files Created & Modified
- **Modified:** 
  - `backend/src/config/settings.py`: Thêm `dify_api_key`, `dify_api_url`, `openai_api_key`.
  - `backend/requirements.txt`: Bổ sung thư viện `requests>=2.31.0`.
- **Created:**
  - `backend/src/knowledge/__init__.py`
  - `backend/src/knowledge/dify_client.py`
  - `backend/src/knowledge/search.py`
  - `backend/src/knowledge/insight_extractor.py`

## Functions Implemented
- **`DifyClient`**: Xử lý Authentication Header và đóng gói phương thức HTTP GET/POST để gọi Dify API.
- **`search_dataset(query, dataset_id)`**: Gọi endpoint retrieve của Dify để tìm kiếm các phân đoạn tài liệu phù hợp (hybrid search & reranking).
- **`retrieve_chunks(document_id)`**: Lấy nội dung thô (chunks) của một văn bản đã nạp trên Dify.
- **`extract_insights(context_text)`**: Giao tiếp với API OpenAI (`gpt-4o-mini`) bằng một System Prompt đặc thù của chuyên gia Content Strategy để rút gọn text thành danh sách 2-3 Insights cốt lõi. (Hỗ trợ Mock Insight nếu chưa có cấu hình KEY).

## Testing
- Import `search_dataset` và `extract_insights` thành công vào App.
- Dependencies (`requests`) đã được cài đặt và kích hoạt chạy thử không bị lỗi biên dịch.

## Result
PASS

## Next Sprint Recommendation
Tiến hành Sprint 5: Angle Module (Sáng tạo góc độ tiếp cận dựa trên Knowledge).
