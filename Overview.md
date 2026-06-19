# Unified Content Agent
## Project Overview

### Mục tiêu dự án

Unified Content Agent là một hệ thống AI Content Pipeline chạy local, giúp chuyển đổi tri thức từ Dify và ý tưởng của người dùng thành nội dung hoàn chỉnh sẵn sàng xuất bản.

Hệ thống tập trung vào:

- Tăng tốc quy trình sản xuất content
- Giảm thao tác thủ công
- Đảm bảo chất lượng đầu ra
- Duy trì vai trò kiểm duyệt cuối cùng của con người

Đây không phải là hệ thống AgentOS phức tạp hay Autonomous AI Platform.

Đây là một Pipeline System đơn giản, dễ triển khai, dễ bảo trì và phù hợp với cá nhân hoặc đội nhóm nhỏ.

---

# Người dùng làm gì?

Người dùng chỉ cần:

## Cách 1: Nhập ý tưởng

Ví dụ:

```text
Khuyết điểm của bạn là gì khi đi phỏng vấn?
```

## Cách 2: Chọn tri thức từ Dify

Ví dụ:

- Sách giao tiếp
- Tâm lý học
- Self-help
- Kỹ năng mềm

Sau đó nhấn:

```text
Generate Content
```

---

# Hệ thống làm gì?

Sau khi nhận yêu cầu, hệ thống tự động thực hiện toàn bộ pipeline.

---

## Bước 1 — Knowledge Retrieval

Nguồn dữ liệu:

```text
Dify Dataset
    ↓
Documents
    ↓
Chunks
```

Mục tiêu:

- Tìm các đoạn tri thức liên quan
- Trích xuất ngữ cảnh phù hợp với chủ đề

Output:

```json
[
  "chunk_1",
  "chunk_2",
  "chunk_3"
]
```

---

## Bước 2 — Insight Extraction

Từ các chunk đã lấy được, AI phân tích:

- Pain Point
- Emotion
- Insight

Ví dụ:

```json
{
  "pain_point": "Người trẻ sợ bị đánh giá",
  "emotion": "Lo lắng",
  "insight": "Khuyết điểm có thể trở thành cơ hội thể hiện sự trưởng thành"
}
```

---

## Bước 3 — Angle Generation

Sinh nhiều góc tiếp cận khác nhau.

Ví dụ:

### Angle 1

```text
Khuyết điểm khi phỏng vấn
```

### Angle 2

```text
Tại sao câu hỏi này khiến nhiều ứng viên thất bại?
```

### Angle 3

```text
Biến điểm yếu thành lợi thế
```

Hệ thống chọn angle phù hợp nhất.

---

## Bước 4 — Caption Generation

Dựa trên angle đã chọn.

Sinh nội dung theo cấu trúc:

```text
Hook
↓
Story
↓
Insight
↓
CTA
```

Ví dụ:

```text
"Khuyết điểm của bạn là gì?"

Đây là câu hỏi khiến rất nhiều người...
...
```

Output:

- Instagram Caption
- Threads Caption
- Hashtags

---

## Bước 5 — Caption Evaluation

Caption được AI đánh giá theo các tiêu chí:

- Hook
- Emotion
- Insight
- CTA
- Clarity

Ví dụ:

```json
{
  "score": 7.2,
  "pass": false
}
```

Nếu chưa đạt:

```text
CTA yếu
```

Hệ thống chỉ sửa phần CTA thay vì tạo lại toàn bộ caption.

Mục tiêu:

- Tiết kiệm token
- Giữ lại nội dung tốt đã tạo

---

## Bước 6 — Image Prompt Builder

Từ caption, hệ thống tạo prompt sinh ảnh.

Ví dụ:

```text
Glasses Girl
Anime Style
Ghibli Inspired
Office Hallway
Soft Pastel Colors
```

---

## Bước 7 — Image Generation

Gọi mô hình sinh ảnh.

Ví dụ:

```text
NVIDIA Image Generation
```

Output:

```text
1080x1080
```

Ảnh hoàn chỉnh phục vụ đăng mạng xã hội.

---

## Bước 8 — Image Evaluation

Ảnh được đánh giá theo:

- Character Consistency
- Composition
- Style Consistency
- Color Palette

Nếu chưa đạt:

```text
Prompt chưa đủ chính xác
```

Hệ thống:

- Điều chỉnh prompt
- Sinh lại ảnh

Cho đến khi đạt ngưỡng yêu cầu.

---

## Bước 9 — Draft Creation

Tổng hợp toàn bộ kết quả thành Draft.

Draft bao gồm:

```text
Angle

Instagram Caption

Threads Caption

Hashtags

Image

Evaluation Result
```

---

# Human Review

Tất cả nội dung phải được duyệt thủ công trước khi xuất bản.

Trang:

```text
/review
```

Người dùng xem:

- Ảnh
- Caption
- Điểm đánh giá

Các hành động:

### Approve

Phê duyệt nội dung.

### Reject

Từ chối nội dung.

### Regenerate Caption

Tạo lại caption.

### Regenerate Image

Tạo lại ảnh.

---

# Sau khi Approve

Hệ thống thực hiện:

## Markdown Export

Sinh file Markdown:

```markdown
# Tiêu đề

## Caption

...

## Hashtags

...

## Image

...
```

---

## Publish

Xuất bản lên:

- Instagram
- Threads

---

# Workflow Tổng Thể

```text
User Input
        │
        ▼
Knowledge Retrieval (Dify)
        │
        ▼
Insight Extraction
        │
        ▼
Angle Generation
        │
        ▼
Caption Generation
        │
        ▼
Caption Evaluation
        │
   Pass ?
    │
 ┌──┴──┐
 │ No  │
 ▼     │
Retry  │
 │     │
 └─────┘
        │
        ▼
Image Prompt Builder
        │
        ▼
Image Generation
        │
        ▼
Image Evaluation
        │
   Pass ?
    │
 ┌──┴──┐
 │ No  │
 ▼     │
Retry  │
 │     │
 └─────┘
        │
        ▼
Draft Creation
        │
        ▼
Human Review
        │
 ┌──────┴──────┐
 │ Approve     │
 │ Reject      │
 │ Regenerate  │
 └──────┬──────┘
        │
        ▼
Markdown Export
        │
        ▼
Publish
```

---

# Tóm tắt một câu

> Unified Content Agent là hệ thống AI Content Pipeline sử dụng Dify làm kho tri thức, tự tạo caption và hình ảnh, tự đánh giá chất lượng, sau đó đưa cho con người duyệt trước khi xuất bản lên các nền tảng mạng xã hội.