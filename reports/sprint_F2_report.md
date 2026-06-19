# Sprint F2 Report (Frontend ↔ Backend Integration)

## Objective
Kết nối Frontend (Next.js) với Backend API (FastAPI) để xây dựng giao diện người dùng hoàn chỉnh, cho phép xem bản thảo, duyệt/từ chối và kích hoạt pipeline từ trình duyệt.

## Files Created/Modified

**Backend:**
- `backend/src/main.py` [MODIFIED] — Thêm CORS Middleware cho phép `localhost:3000`

**Frontend:**
- `frontend/src/lib/api.ts` [NEW] — API Client tập trung: types + fetch functions cho toàn bộ endpoints
- `frontend/src/app/page.tsx` [MODIFIED] — Dashboard cập nhật số liệu thực từ API
- `frontend/src/app/drafts/page.tsx` [NEW] — Trang duyệt bản thảo
- `frontend/src/app/pipelines/page.tsx` [NEW] — Trang chạy pipeline

## Functions Implemented

**`lib/api.ts`**
- `fetchDrafts()` → `GET /api/drafts/`
- `fetchDraft(id)` → `GET /api/drafts/{id}`
- `approveDraft(id)` → `POST /api/drafts/{id}/approve`
- `rejectDraft(id)` → `POST /api/drafts/{id}/reject`
- `rerunPipeline(topic, platform)` → `POST /api/drafts/rerun`

## UI Implemented

**Dashboard (`/`)**
- 3 stat cards: Tổng bài viết / Đã duyệt / Chờ duyệt (dữ liệu thực từ API)
- 2 quick action buttons: Chạy Pipeline Mới + Duyệt Bản Thảo
- Recent activity list: 5 bản thảo gần nhất với badge trạng thái màu

**Duyệt Bản Thảo (`/drafts`)**
- Layout Master-Detail: danh sách card bên trái + detail panel bên phải
- Draft Card: tiêu đề, badge trạng thái (`pending`=vàng / `approved`=xanh / `rejected`=đỏ), ngày tạo
- Detail Panel: Angle, Caption đầy đủ, Score bars 5 tiêu chí Caption Evaluation, Score bars 4 tiêu chí Image Evaluation, Image Prompt
- Nút **Duyệt** và **Từ chối** gọi API thật, cập nhật UI ngay lập tức + toast notification

**Chạy Pipeline (`/pipelines`)**
- Textarea nhập chủ đề
- Chọn nền tảng: Instagram / Threads (toggle button)
- Nút **Chạy Pipeline** với loading spinner
- Step Visualizer: 7 bước hiển thị trạng thái (idle → loading animate-pulse → success checkmark)
- Result card: hiển thị Draft ID mới + link "Xem bản thảo vừa tạo"

## Testing
- Đã mở trình duyệt và xác nhận cả 3 trang render đúng
- Dashboard hiển thị đúng số `1` bản thảo từ API
- Trang Drafts hiển thị card "Draft Thử Nghiệm" với badge "Đã từ chối"
- Trang Pipelines hiển thị form đầy đủ với Step Visualizer 7 bước

## Result
PASS

## Next Sprint Recommendation
- **Sprint F3**: Cải thiện UX — active state cho sidebar navigation, trang Settings kết nối API
- hoặc tiếp tục **Sprint 13**: Instagram Publish (cần Instagram Access Token)
