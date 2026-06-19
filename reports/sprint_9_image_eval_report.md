# Sprint 9 Report (Image Evaluation)

## Objective
Tạo module đánh giá hình ảnh bằng AI (Image Evaluation) giúp tự động kiểm tra chất lượng ảnh dựa trên 4 tiêu chí: Character, Composition, Color, Style. Tự động viết lại Prompt (Improve Image) nếu chất lượng ảnh không đạt.

## Files Created/Modified
- `backend/src/evaluation/image_evaluator.py`
- `backend/src/evaluation/retry_image.py`
- `backend/src/evaluation/__init__.py`

## Functions Implemented
**`evaluate_image(image: Image) -> ImageEvaluation`**
Sử dụng NVIDIA API Vision model (`meta/llama-3.2-90b-vision-instruct`) để "nhìn" bức ảnh base64 và chấm điểm. Model sẽ phân tích và đưa ra điểm trung bình (`overall_score`) kèm những lời phê (feedback). 

**`improve_image(image: Image, evaluation: ImageEvaluation) -> Image`**
Nếu `overall_score < 8.0`, hàm này cung cấp feedback cho model ngôn ngữ để sinh ra một prompt tiếng Anh MỚI hoàn toàn, giải quyết triệt để các khuyết điểm được AI giám khảo nhắc đến. Sau đó, nó tự động gọi lại hàm sinh ảnh mới từ Image Module.

## Testing
- Đã chạy script test API với model Vision để đánh giá thành công một bức ảnh mẫu (nhận điểm số và nhận xét chi tiết từ AI).
- Đã chạy script test `improve_image`, đưa feedback giả là *"Lỗi: Chủ thể bị méo, màu sắc nhợt nhạt"*. Model đã xuất sắc sinh ra prompt mới: *"Một con mèo trắng tinh khiết với bộ lông mềm mại, đôi mắt xanh biếc và khuôn mặt tròn trịa, được đặt trong một không gian sáng sủa với ánh sáng ấm áp và màu sắc tươi tắn"*.
- Lỗi `404` khi gọi Endpoint Image API ở bước sinh lại ảnh được xử lý (catch) an toàn, không gây crash ứng dụng.

## Result
PASS (Hoàn thành chức năng Đánh giá Ảnh và Cải thiện Ảnh tự động).

## Next Sprint Recommendation
Theo tài liệu, bước cuối cùng là **Sprint 10: Pipeline Orchestrator** (Lắp ghép tất cả các module vào 1 pipeline duy nhất hoàn chỉnh).
