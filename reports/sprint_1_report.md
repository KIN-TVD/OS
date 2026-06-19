# Sprint 1 Report

## Objective
Khởi tạo project Backend cơ bản theo yêu cầu.
- Tạo cấu trúc thư mục.
- Tạo FastAPI server.
- Tạo file config.
- Tạo logger.
- Không viết business logic.

## Files Created
- `backend/src/main.py`
- `backend/src/api.py`
- `backend/src/config/settings.py`
- `backend/src/utils/logger.py`
- `backend/requirements.txt`

## Functions Implemented
**read_root()**
Trả về message chào mừng của API tại root (`/`).

**startup_event()**
Ghi log (bằng logger đã thiết lập) khi ứng dụng bắt đầu khởi động.

**health_check()**
Kiểm tra tình trạng sức khỏe của API tại endpoint `/api/health`.

**setup_logger()**
Cấu hình logger tiêu chuẩn (console output) để sử dụng trong toàn bộ hệ thống.

## API Added
- `GET /`
- `GET /api/health`

## Testing
- Tạo môi trường ảo (virtualenv) trong thư mục `backend/.venv`.
- Cài đặt thành công các thư viện từ `requirements.txt`.
- App chạy không phát sinh lỗi khởi tạo (`import src.main` thành công).

## Result
PASS

## Next Sprint Recommendation
Tiến hành Sprint 2: Tạo schema cho hệ thống (angle, caption, image, evaluation, draft) bằng Pydantic.
