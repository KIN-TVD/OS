# Frontend Sprint F3 Report (Mission Page)

## Objective
Xây dựng trang `/missions` hiển thị danh sách nhiệm vụ với Mission ID, Status, tiến độ (progress bar) và điểm đánh giá.

## Files Created
- `frontend/src/app/missions/page.tsx`
- `backend/src/routers/missions.py`
- `backend/src/api.py` [MODIFIED]

## API Added
- `GET /api/missions/` — Backend tổng hợp dữ liệu từ drafts JSON, tính progress tự động

## UI Implemented
- 3 stat cards: Tổng / Đã duyệt / Chờ duyệt
- Table: Mission ID (mono), Tiêu đề, Badge trạng thái màu, Caption score, Image score, Progress bar, Ngày tạo
- Empty state và loading skeleton

## Testing
- Trang load và hiển thị đúng 1 mission từ API backend

## Result
PASS
