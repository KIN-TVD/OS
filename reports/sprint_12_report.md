# Sprint 12 Report (Review API)

## Objective
Xây dựng các HTTP Endpoints (FastAPI) cho phép Frontend tương tác trực tiếp với hệ thống: xem danh sách bản nháp, duyệt, từ chối, và kích hoạt lại pipeline.

## Files Created/Modified
- `backend/src/routers/__init__.py` [NEW]
- `backend/src/routers/drafts.py` [NEW]
- `backend/src/api.py` [MODIFIED]

## API Endpoints Added

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| `GET` | `/api/drafts/` | Lấy danh sách tất cả bản nháp (summary) |
| `GET` | `/api/drafts/{draft_id}` | Lấy chi tiết đầy đủ của 1 bản nháp |
| `POST` | `/api/drafts/{draft_id}/approve` | Duyệt bản nháp → status = `approved` + export Markdown |
| `POST` | `/api/drafts/{draft_id}/reject` | Từ chối bản nháp → status = `rejected` |
| `POST` | `/api/drafts/rerun` | Kích hoạt lại pipeline với topic mới |

## Testing (Live API)

**`GET /api/health`**
```json
{"status": "ok", "message": "AgentOS API is running"}
```

**`GET /api/drafts/`**
```json
[{"id": "test-123", "title": "Draft Thử Nghiệm", "status": "pending", "created_at": "..."}]
```

**`POST /api/drafts/test-123/approve`**
```json
{"success": true, "message": "Draft approved. Markdown at data/outputs/test-123.md", "draft_id": "test-123"}
```

**`POST /api/drafts/test-123/reject`**
```json
{"success": true, "message": "Draft rejected.", "draft_id": "test-123"}
```
Status được cập nhật trực tiếp vào file JSON trên disk.

## Result
PASS (Tất cả 5 endpoints hoạt động đúng, status persist xuống JSON sau mỗi action)

## Next Sprint Recommendation
Theo tài liệu, bước tiếp theo là **Sprint 13: Instagram Publish** — tạo `publish/instagram_client.py` với hàm `publish_instagram()`.
