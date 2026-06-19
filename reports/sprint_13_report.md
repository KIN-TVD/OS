# Sprint 13 Report (Instagram Publish)

## Objective
Tạo module `instagram_client.py` để đăng bài tự động lên Instagram thông qua Meta Graph API.

## Files Created
- `backend/src/publish/instagram_client.py`
- `backend/src/routers/publish.py` (endpoint)
- `backend/src/config/settings.py` [MODIFIED]
- `backend/.env` [MODIFIED]

## Functions Implemented
**`publish_instagram(caption: str, image: Image) -> dict`**
Triển khai đúng Meta Graph API 2-step flow:
1. `POST /{user_id}/media` — Tạo media container với `image_url` + `caption`
2. `POST /{user_id}/media_publish` — Publish container bằng `creation_id`

Trả về: `success`, `media_id`, `permalink`

## API Added
- `POST /api/publish/instagram` — Nhận `draft_id`, load Draft, kiểm tra status='approved', gọi `publish_instagram()`

## Configuration
Thêm vào `settings.py`: `instagram_access_token`, `instagram_user_id`
Thêm vào `.env`: `INSTAGRAM_ACCESS_TOKEN=`, `INSTAGRAM_USER_ID=` (chờ điền token thật)

## Testing
- Import thành công
- Fallback graceful khi chưa có token: trả về `{"success": false, "mock": true, "error": "..."}`
- Không crash ứng dụng khi thiếu credentials

## Result
PASS (Code logic hoàn chỉnh, chờ token thật để test live)
