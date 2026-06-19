# Sprint 14 Report (Threads Publish)

## Objective
Tạo module `threads_client.py` để đăng bài tự động lên Threads thông qua Meta Threads API.

## Files Created
- `backend/src/publish/threads_client.py`

## Files Modified
- `backend/src/routers/publish.py` — Thêm endpoint `/threads`
- `backend/src/publish/__init__.py` — Export `publish_threads`
- `backend/.env` — Thêm `THREADS_ACCESS_TOKEN`, `THREADS_USER_ID`

## Functions Implemented
**`publish_threads(text: str) -> dict`**
Triển khai Threads API 2-step flow:
1. `POST /{user_id}/threads` với `media_type=TEXT` + `text`
2. `POST /{user_id}/threads_publish` với `creation_id`

## API Added
- `POST /api/publish/threads` — Nhận `draft_id`, ưu tiên caption có platform='threads', fallback về caption đầu tiên

## Testing
- Import thành công
- Fallback graceful khi chưa có token: `{"success": false, "mock": true}`

## Result
PASS (Code logic hoàn chỉnh, chờ token thật để test live)
