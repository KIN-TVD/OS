# Frontend Sprint F4 Report (Draft Review)

## Objective
Xây dựng trang `/review` với layout 2 cột: Image Preview bên trái, Caption + Evaluation + Action Buttons bên phải.

## Files Created
- `frontend/src/app/review/page.tsx`

## API Used
- `GET /api/drafts/` — Lấy danh sách để chọn
- `GET /api/drafts/{id}` — Chi tiết
- `POST /api/drafts/{id}/approve`
- `POST /api/drafts/{id}/reject`
- `POST /api/drafts/rerun`

## UI Implemented
- Selector bar: chọn nhanh bản thảo bằng pill button (badge trạng thái màu)
- Cột trái: Image preview (base64), Image Prompt, Image Evaluation (4 tiêu chí score bar)
- Cột phải: Caption text, Caption Evaluation (5 tiêu chí score bar + AI comment)
- 3 nút: Từ chối (đỏ) / Re-run (trắng) / Duyệt (xanh) — loading spinner + disabled state
- Toast notification

## Testing
- Mở trang /review, chọn "Draft Thử Nghiệm" — hiển thị đầy đủ 2 cột với các nút action

## Result
PASS
