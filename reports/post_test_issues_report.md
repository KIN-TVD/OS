# Báo cáo các vấn đề sau khi chạy End-to-End Test

Sau khi kiểm tra toàn bộ luồng dữ liệu thực tế với các Model API của NVIDIA, tôi đã phát hiện ra **3 vấn đề chính** cần khắc phục để hệ thống hoạt động ổn định và chính xác 100%.

## 1. Lỗi Parse JSON khi chấm điểm hình ảnh (Image Evaluator)
- **Hiện tượng:** Ở kết quả Markdown, phần đánh giá hình ảnh bị lỗi `Error: Expecting value: line 1 column 1 (char 0)` và trả về kết quả `FAIL` với điểm 0.
- **Nguyên nhân:** 
  - Trong `src/evaluation/image_evaluator.py`, tham số `max_tokens` đang được set quá thấp (`256`). Prompt yêu cầu model chấm điểm 4 tiêu chí và viết nhận xét chi tiết (comments). Khi lượng chữ vượt quá 256 tokens, model bị cắt ngang giữa chừng khiến chuỗi JSON bị đứt đoạn, dẫn đến lỗi `JSONDecodeError`.
  - Một nguyên nhân phụ khác là đôi khi model Llama-3.2-Vision không bọc kết quả trong thẻ ` ```json ` mà trả về text lẫn lộn, khiến đoạn mã cắt chuỗi bị sai.
- **Cách khắc phục:** 
  - Tăng `max_tokens` lên `1024`.
  - Nâng cấp bộ parse JSON mạnh hơn để tự động tìm ngoặc nhọn `{...}` thay vì chỉ dựa vào ` ```json `.

## 2. Prompt sinh ảnh bị dịch sang tiếng Việt (Prompt Builder)
- **Hiện tượng:** Mặc dù System Prompt yêu cầu rõ: `"generate a highly detailed, descriptive image generation prompt in English"`, nhưng AI lại sinh ra: `"Một bức ảnh nghệ thuật trừu tượng với màu sắc pastel mềm mại..."` (tiếng Việt).
- **Nguyên nhân:** Model `meta/llama-3.1-70b-instruct` có xu hướng bị cuốn theo ngôn ngữ của Input Text (Caption đang là tiếng Việt), khiến nó "quên" yêu cầu trả về tiếng Anh trong System Prompt.
- **Cách khắc phục:**
  - Bổ sung chỉ thị cực mạnh vào phần cuối của System Prompt: `WARNING: The "prompt" value MUST BE TRANSLATED TO STRICTLY ENGLISH. Do not use Vietnamese.`

## 3. Quản lý thời gian chờ (Timeout) của Pipeline
- **Hiện tượng:** Lệnh gọi API `/api/drafts/rerun` thực thi các tác vụ sinh nội dung một cách đồng bộ (chạy tuần tự Angle -> Caption -> Image -> Evaluate). Tổng thời gian chờ có thể lên tới 2-3 phút, khiến trình duyệt Frontend hoặc các công cụ gọi HTTP có thể bị Time-out trước khi nhận được kết quả.
- **Cách khắc phục:** 
  - Backend đã có xử lý try/except nhưng ở trình duyệt Frontend có thể bị đứt kết nối nếu chờ quá 60s. Về lâu dài có thể áp dụng kiến trúc Background Task (như Celery/Redis). Trong phạm vi dự án này, cần đảm bảo timeout của axios trên Frontend được thiết lập lớn hơn (e.g., 5 phút).
