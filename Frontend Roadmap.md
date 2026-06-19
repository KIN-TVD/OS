**FRONTEND ROADMAP**

Frontend chỉ bắt đầu sau Sprint 3.

Lý do:

Lúc đó đã có:

- API
- Schema
- Storage

Frontend sẽ có dữ liệu để test.![](Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.001.png)

**FRONTEND SPRINT F1**

Mục tiêu:

Khởi tạo giao diện.

Tech:

- NextJS
- TypeScript
- Tailwind
- Shadcn![](Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.002.png)

Tạo:

frontend/

app/

components/

lib/

types/![](Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.003.png)

Layout:

Sidebar

Topbar

Main Content![ref1]

Pages:

Dashboard

Settings![ref2]

Chưa gọi API.![ref3]

Output:

Frontend chạy được.![ref2]

Report:

reports/frontend\_sprint\_1.md Dừng.![ref1]![ref2]

**FRONTEND SPRINT F2**

Mục tiêu:

Kết nối Backend.![ref4]

Tạo:

lib/api.ts![ref5]

Functions:

getDrafts()

runPipeline()

approveDraft()

rejectDraft()![ref3]

Tạo:

hooks/

useDrafts.ts![ref6]

Test:

Fetch API thành công.![ref3]

Report:

frontend\_sprint\_2.md![ref2]

Dừng.![ref3]

**FRONTEND SPRINT F3**

Mục tiêu:

Mission Page.![ref7]

Page:

/missions![ref4]

Hiển thị:

Mission ID

Status

Created Time

Progress![ref1]

Components:

MissionTable

MissionCard

MissionStatusBadge![ref6]

API:

GET /missions![ref3]

Report:

frontend\_sprint\_3.md![ref2]

Dừng.![ref3]

**FRONTEND SPRINT F4**

Mục tiêu:

Draft Review.![ref7]

Page:

/review![ref4]

Layout:

2 cột.

Cột trái:![ref3]

Image Preview![ref2]

Cột phải:

Caption

Hashtags

Evaluation![ref1]

Buttons:

Approve

Reject

Re-run![ref6]

API:

GET /drafts

POST /approve

POST /reject

POST /rerun![ref1]

Report:

frontend\_sprint\_4.md![ref6]

Dừng.![ref1]

5
**FRONTEND SPRINT F5**

Mục tiêu:

Run Pipeline.![ref8]

Page:

/run![ref7]

Form:

Input Content

Profile

Dataset

Generate![ref8]

Button:

Run Pipeline![ref7]

API:

POST /run![ref4]

Report:

frontend\_sprint\_5.md![ref5]

Dừng.![ref4]

6
**FRONTEND SPRINT F6**

Mục tiêu:

Knowledge Hub.![ref8]

Page:

/knowledge![ref7]

Hiển thị:

Datasets

Documents

Chunks![ref4]

Search Box![ref7]

API:

GET /datasets

GET /documents

POST /search![ref4]

Report:

frontend\_sprint\_6.md![ref5]

Dừng.![ref4]

7
**FRONTEND SPRINT F7**

Mục tiêu:

Evaluation Page.![ref8]

Page:

/evaluations![ref7]

Hiển thị:

Hook Score

Emotion Score

Insight Score

CTA Score

Clarity Score![ref4]

Charts:

Radar Chart

Bar Chart![ref7]

API:

GET /evaluations![ref4]

Report:

frontend\_sprint\_7.md![ref5]

Dừng.![ref4]

8
**FRONTEND SPRINT F8**

Mục tiêu:

Output Page.![ref8]

Page:

/outputs![ref7]

Hiển thị:

Markdown

Instagram

Threads![ref4]

Download Button

Preview Button![ref5]

API:

GET /outputs![ref8]

Report:

frontend\_sprint\_8.md![ref7]

Dừng.![ref8]

**FRONTEND SPRINT F9**

Mục tiêu:

9

Settings.![ref1]

Page:

/settings![ref6]

Tabs:

API Keys

Models

Profiles

Evaluation Rules![ref1]

API:

GET /settings

POST /settings![ref2]

Report:

frontend\_sprint\_9.md![ref1]

Dừng.![ref2]

**FRONTEND SPRINT F10**

Mục tiêu:

Dashboard.![ref4]

Cards:

Draft Count

10

Published Count

Success Rate

Average Score![ref1]

Charts:

Content Trend

Evaluation Trend

Generation Trend![ref6]

API:

Dashboard Summary![ref3]

Report:

frontend\_sprint\_10.md![ref2]

Dừng.![ref3]

**FRONTEND SPRINT F11**

Mục tiêu:

History.![ref7]

Page:

/history![ref4]

Filters:

Date

Status

Profile![ref3]

Search![ref6]

API:

GET /history![ref3]

Report:

frontend\_sprint\_11.md![ref2]

Dừng.![ref3]

**FRONTEND SPRINT F12**

Mục tiêu:

UI Polish.![ref7]

Responsive

Loading State

Skeleton

Error Handling

Empty State

Toast

Dark Mode![ref8]

Report:

frontend\_sprint\_12.md![ref1]

Dừng.![ref2]

**FRONTEND SPRINT F13**

Mục tiêu:

End-to-End Test.![ref4]

Flow:

Run Pipeline

↓

Review Draft

↓

Approve

↓

Publish

↓

History![ref8]

Tạo:

reports/frontend\_final\_report.md![ref7]

Dừng hoàn toàn.

Không thêm chức năng mới.
13

[ref1]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.004.png
[ref2]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.005.png
[ref3]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.006.png
[ref4]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.007.png
[ref5]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.008.png
[ref6]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.009.png
[ref7]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.010.png
[ref8]: Aspose.Words.78667e23-68f4-4336-93fe-79b0ecb9cd96.011.png
