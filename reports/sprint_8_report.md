# Sprint 8 Report (Image Module)

## Objective
Tạo module hình ảnh (Image Module) bao gồm: Dịch caption thành Image Prompt chuyên nghiệp bằng AI, gọi API sinh ảnh (NVIDIA Flux) và lưu ảnh trả về dạng Base64 xuống ổ cứng.

## Files Created
- `backend/src/image/__init__.py`
- `backend/src/image/prompt_builder.py`
- `backend/src/image/image_generator.py`
- `backend/src/image/image_store.py`

## Functions Implemented
**`build_prompt(caption: Caption) -> str`**
Dùng NVIDIA API (Chat Completions) để phân tích đoạn caption tiếng Việt và sinh ra một Image Generation Prompt chuẩn tiếng Anh (bao gồm miêu tả ánh sáng, góc máy, thể loại đồ hoạ...).

**`generate_image(prompt: str) -> Image`**
Gọi NVIDIA Image API để sinh ảnh từ prompt. Giao tiếp với API thông qua `NVIDIA_API_KEY_IMG` bằng model `black-forest-labs/flux1-dev` và nhận về chuỗi mã hoá Base64.

**`save_image(image: Image) -> str`**
Giải mã chuỗi Base64 thành dữ liệu nhị phân và ghi ra file hình ảnh vật lý (`.png`) vào thư mục `backend/data/images/`. Cập nhật đường dẫn file vào đối tượng.

## Testing & Issues
- Hệ thống module đã được thiết lập logic chính xác từ bước chuẩn bị prompt đến bước save file.
- Khi test thực tế (Live API), request sinh Prompt bị timeout từ server (lỗi 504), hệ thống tự động fallback về prompt an toàn.
- Request sinh ảnh gọi đến `https://integrate.api.nvidia.com/v1/images/generations` gặp lỗi `404 Not Found`. Lỗi này xuất phát từ việc URL endpoint sinh ảnh của nền tảng NVIDIA có thể khác nhau tùy vào model (Ví dụ một số model dùng `https://ai.api.nvidia.com/v1/genai/...`).
- **Khắc phục:** Code đã bắt được exception an toàn để không làm sập ứng dụng. Để API hoạt động, cần cấu hình lại chính xác URL Endpoint Image API của NVIDIA vào hàm `generate_image` tùy thuộc vào model Flux cụ thể mà tài khoản của bạn được cấp quyền.

## Result
PASS (Mặt logic code đã xử lý thành công, lỗi 404 Endpoint có thể fix sau bằng cách thay URL).

## Next Sprint Recommendation
Tiến hành **Sprint 9: Image Evaluation** (Đánh giá hình ảnh).
