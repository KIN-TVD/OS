# Sprint 11 Report (Markdown Export)

## Objective
Tạo module xuất nội dung bài viết (Draft) thành file Markdown (.md) có cấu trúc đầy đủ để con người có thể đọc, review trước khi đăng bài lên mạng xã hội.

## Files Created
- `backend/src/publish/__init__.py`
- `backend/src/publish/markdown_exporter.py`

## Functions Implemented
**`export_markdown(draft: Draft) -> str`**
Nhận vào đối tượng `Draft` hoàn chỉnh. Tạo file `.md` chứa đầy đủ thông tin được trình bày rõ ràng theo từng Section có emoji:
- **Header**: ID, trạng thái, ngày tạo
- **📐 Góc Độ**: Tiêu đề angle, mô tả, điểm confidence
- **✍️ Nội dung bài viết**: Caption cho từng nền tảng
- **📊 Đánh giá Caption**: Bảng điểm 5 tiêu chí (Hook/Emotion/Insight/CTA/Clarity) + nhận xét AI
- **🖼️ Hình ảnh**: Image prompt, đường dẫn file + bảng điểm 4 tiêu chí (Character/Composition/Color/Style) + nhận xét AI
- **Footer**: Timestamp tạo file

Lưu file tại `backend/data/outputs/<draft_id>.md` và trả về đường dẫn.

## Testing
Đã chạy test với Draft mẫu đầy đủ dữ liệu (Angle + Caption + Image + 2 bộ Evaluation). Kết quả:
- File `data/outputs/test_export_01.md` được tạo thành công
- Nội dung bảng điểm, emoji, nhận xét hiển thị đúng định dạng Markdown
- Caption PASS (8.3/10), Image PASS (8.0/10) được render chính xác

## Result
PASS

## Next Sprint Recommendation
Tiến hành **Sprint 12: Review API** – tạo các HTTP Endpoints (FastAPI) để Frontend có thể:
- `GET /drafts` – Lấy danh sách bản nháp
- `POST /approve` – Duyệt bản nháp
- `POST /reject` – Từ chối bản nháp
- `POST /rerun` – Chạy lại pipeline cho bản nháp mới
