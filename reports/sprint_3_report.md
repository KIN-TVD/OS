# Sprint 3 Report

## Objective
Tạo Storage Layer để lưu trữ dữ liệu JSON cục bộ và phân chia rõ ràng thư mục dữ liệu nhằm chuẩn bị cho việc tích hợp vào Database (Table) sau này.

## Files & Directories Created
- **Directories:** 
  - `backend/data/drafts/`
  - `backend/data/images/`
  - `backend/data/logs/`
  - `backend/data/outputs/`
- **Files:**
  - `backend/src/storage/json_utils.py`
  - `backend/src/storage/file_utils.py`

## Functions Implemented
**save_json(filepath, data)**
Lưu một dictionary thành file JSON (có indent chuẩn và hỗ trợ unicode).

**load_json(filepath)**
Đọc file JSON từ đường dẫn tĩnh và trả về dictionary. Nếu không tồn tại thì trả về dictionary rỗng.

**save_draft(draft_id, draft_data)**
Tạo abstraction pattern: Lấy input là dictionary hoặc Pydantic object `Draft`, định tuyến lưu file đến `backend/data/drafts/{draft_id}.json`. Logic này được thiết kế để sau này có thể dễ dàng sửa lại thành câu lệnh `INSERT INTO / UPDATE` database.

**load_draft(draft_id)**
Tải một `Draft` bằng ID. Sau này sẽ dễ dàng thay bằng câu lệnh `SELECT * FROM drafts WHERE id = ...`.

## Testing
- Import `save_draft` và `load_draft`, sử dụng model `Draft(id='test-123', title='Draft Thử Nghiệm')`.
- Đã lưu xuống file `test-123.json` và tải lại thành công title từ JSON (không mất mát hay sai sót metadata).

## Result
PASS

## Next Sprint Recommendation
Tiến hành Sprint 4: Knowledge Module (Tìm kiếm và trích xuất thông tin). Hoặc chúng ta có thể tiến hành thiết lập **Frontend Sprint F1** (Khởi tạo giao diện) vì điều kiện (API, Schema, Storage) đã được đáp ứng xong.
