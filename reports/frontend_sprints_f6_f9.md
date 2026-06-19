# Frontend Sprints F6-F9 Reports

## Sprint F6: Knowledge Hub
- **Objective:** Xây dựng trang `/knowledge` hiển thị Datasets và khung tìm kiếm.
- **Backend:** Thêm `routers/knowledge.py` cung cấp 3 API (`GET /datasets`, `GET /documents`, `POST /search`). Tích hợp sẵn với Dify API hoặc trả về mock data nếu thiếu token.
- **Frontend:** Xây dựng `app/knowledge/page.tsx` hiển thị thống kê Dataset và thực hiện tìm kiếm hybrid.
- **Result:** PASS

## Sprint F7: Evaluation Dashboard
- **Objective:** Xây dựng trang `/evaluations` trực quan hóa điểm số đánh giá.
- **Backend:** Thêm `routers/evaluations.py` thống kê, tính điểm trung bình từ các file JSON trong `drafts`.
- **Frontend:** Cài đặt `recharts`, xây dựng `app/evaluations/page.tsx` với Radar Chart (cho Caption & Image) và Bar Chart (Lịch sử điểm số).
- **Result:** PASS

## Sprint F8: Outputs Page
- **Objective:** Xây dựng trang `/outputs` quản lý file Markdown đã xuất.
- **Backend:** Thêm `routers/outputs.py` đọc thư mục `data/outputs/` và nội dung file.
- **Frontend:** Thêm thư viện `react-markdown`, xây dựng `app/outputs/page.tsx` với danh sách file, preview markdown và nút Download.
- **Result:** PASS

## Sprint F9: Settings Page
- **Objective:** Xây dựng trang `/settings` quản lý API Keys.
- **Backend:** Thêm `routers/settings.py` đọc `.env` (qua `settings.py`) và che một phần key bảo mật.
- **Frontend:** Xây dựng `app/settings/page.tsx` với giao diện Tabs chuyên nghiệp.
- **Result:** PASS

---
Tất cả các API Router đều đã được mount vào `api.py`. Thanh điều hướng (Sidebar) đã được cập nhật đầy đủ các link đến tính năng mới.
