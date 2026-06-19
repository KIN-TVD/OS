# Sprint 2 Report

## Objective
Tạo schema cho hệ thống bằng thư viện Pydantic.

## Files Created
- `backend/src/schemas/__init__.py`
- `backend/src/schemas/angle.py`
- `backend/src/schemas/caption.py`
- `backend/src/schemas/image.py`
- `backend/src/schemas/evaluation.py`
- `backend/src/schemas/draft.py`

## Schema Implemented
**Angle**
Đại diện cho góc độ tiếp cận (chứa title, description, confidence_score).

**Caption**
Đại diện cho nội dung bài viết (chứa text, hashtags, platform).

**Image**
Đại diện cho thông tin hình ảnh tạo ra (chứa prompt, url, base64_data, format).

**CaptionEvaluation & ImageEvaluation**
Đại diện cho các tiêu chí đánh giá cho cả text và hình ảnh (hook_score, emotion_score, insight_score, character_score, composition_score,...).

**Draft**
Model bản thảo tổng hợp (chứa id, title, status, created_at, angle, captions, image, evaluations).

## Testing
- Import thành công toàn bộ models vào môi trường Python.
- Pydantic kiểm tra không có lỗi cú pháp hoặc typing circular dependencies.

## Result
PASS

## Next Sprint Recommendation
Tiến hành Sprint 3: Tạo Storage Layer (với file_utils.py, json_utils.py để lưu và đọc bản thảo, hình ảnh).
