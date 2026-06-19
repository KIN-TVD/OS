# Sprint 7 Report (Caption Evaluation)

## Objective
Tạo module tự động đánh giá và tự động cải thiện nội dung (Caption Evaluation) bằng cách giao tiếp với NVIDIA API làm giám khảo.

## Files Created
- `backend/src/evaluation/__init__.py`
- `backend/src/evaluation/caption_evaluator.py`
- `backend/src/evaluation/retry_caption.py`

## Schema Update
- Thay đổi code để tuân thủ chính xác Schema `CaptionEvaluation` đã thiết kế từ trước (chứa các trường `overall_score` và `comments` thay vì `score`/`feedback`).

## Functions Implemented
**`evaluate_caption(caption) -> CaptionEvaluation`**
Sử dụng NVIDIA API đóng vai trò giám khảo. Nhận đầu vào là nội dung bài viết và nền tảng. Đánh giá dựa trên 5 tiêu chí: Hook, Emotion, Insight, CTA, Clarity. Trả về điểm tổng quát (`overall_score`) và bình luận chi tiết (`comments`).

**`improve_caption(caption, evaluation) -> Caption`**
Nếu điểm đánh giá `< 8.0`, hàm này sẽ được gọi. Nó cung cấp lại văn bản gốc và những bình luận phê bình (feedback) cho NVIDIA API để AI viết lại/sửa đổi nội dung (retry). Giữ lại văn phong và chỉ sửa lỗi.

## Testing — Live NVIDIA API
Đã chạy thử nghiệm thực tế với 1 đoạn caption cố ý viết tệ: *"Bài viết này nói về AI. Nó rất hay. Mọi người nên đọc nhé."*

**Kết quả Evaluate:**
- **Score:** 3.0
- **Feedback AI:** "Caption này cần cải thiện đáng kể. Câu mở đầu không đủ hấp dẫn, không chạm đến cảm xúc người đọc và không cung cấp thông tin sâu sắc. Lời kêu gọi hành động cũng không rõ ràng..."

**Kết quả Cải thiện (Retry):**
AI đã sinh ra caption mới tốt hơn nhiều: *"Khám phá thế giới AI đầy tiềm năng! Bạn đã sẵn sàng để bước vào kỷ nguyên mới của công nghệ thông minh? Bài viết này sẽ mang đến cho bạn cái nhìn sâu sắc về những khả năng và ứng dụng của AI..."*

## Result
PASS (Các module hoạt động tốt, NVIDIA API không gặp Timeout khi tăng thời gian chờ lên 60s).

## Next Sprint Recommendation
Tiến hành Sprint tiếp theo theo thứ tự trong tài liệu: **Sprint 8: Image Module** (Sinh ảnh và xử lý ảnh).
