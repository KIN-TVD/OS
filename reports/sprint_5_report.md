# Sprint 5 Report

## Objective
Tạo Angle Module để tự động sinh ra 3 góc độ tiếp cận nội dung và chọn lọc góc tốt nhất bằng AI.

## Files Created
- `backend/src/angle/__init__.py`
- `backend/src/angle/angle_generator.py`
- `backend/src/angle/angle_selector.py`

## Functions Implemented
**`generate_angles(insights, topic) -> List[Angle]`**
Nhận vào topic và danh sách insights, gọi NVIDIA API (`meta/llama-3.1-70b-instruct`) với System Prompt được thiết kế để tạo ra đúng 3 góc độ đa dạng (cảm xúc, giáo dục, kết quả). Trả về `List[Angle]` theo schema Pydantic đã định nghĩa ở Sprint 2. Có fallback mock khi chưa cấu hình API Key.

**`select_best_angle(angles, criteria) -> Angle`**
Nhận vào danh sách Angle và tiêu chí chọn lựa (mặc định: engagement), gọi NVIDIA API để phân tích và đưa ra quyết định. Có fallback thông minh (chọn angle có `confidence_score` cao nhất) khi API không khả dụng.

## Testing — Live NVIDIA API
Đã chạy thử nghiệm thực tế với topic "Xu hướng content marketing 2025":

| # | Title | Confidence |
|---|-------|-----------|
| 1 | Tâm Hồn Sáng Tạo: Khi AI Đưa Nội Dung Đến Thế Hệ Mới | 0.80 |
| 2 | Bí Quyết Tạo Video Ngắn Hiệu Quả: 5 Mẹo Để Tăng Tương Tác | 0.90 |
| 3 | Nâng Tầm Nội Dung: Cách Tăng 300% Tương Tác Với Video Ngắn | 0.85 |

**Best angle được chọn:** #3 — "Nâng Tầm Nội Dung: Cách Tăng 300% Tương Tác Với Video Ngắn"  
**Reasoning:** "Angle 3 has the most specific and impressive engagement metric, making it the most compelling option."

## Result
PASS

## Next Sprint Recommendation
Tiến hành Sprint 9: Caption Module (generate_caption, generate_hashtags, thread_generator).
