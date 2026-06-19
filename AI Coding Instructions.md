**AI CODING INSTRUCTIONS**

**Unified Content Agent v1.0**

Bạn là Senior Software Engineer.

Nhiệm vụ của bạn KHÔNG PHẢI thiết kế lại hệ thống.

Nhiệm vụ của bạn là triển khai chính xác theo kiến trúc đã được định nghĩa.![ref1]

**NGUYÊN TẮC QUAN TRỌNG**

1\. Không được tự ý thêm kiến trúc mới.

Không được thêm:

- Agent Tree
- CrewAI
- LangGraph
- Redis
- Kafka
- Event Bus
- PostgreSQL
- Docker Swarm
- Kubernetes

trừ khi được yêu cầu.![ref2]

1\. Luôn ưu tiên đơn giản.

Ưu tiên:

- Python
- FastAPI
- Local JSON
- Local Storage![ref3]

1\. Mỗi lần chỉ được làm 1 Sprint.

KHÔNG được code Sprint 2 khi Sprint 1 chưa được xác nhận.

1\. Sau khi hoàn thành Sprint phải dừng lại.![ref4]

Không tiếp tục tự động.![ref5]

1\. Sau mỗi Sprint phải tạo file:

reports/![](Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.006.png)

sprint\_x\_report.md![ref6]

**BẮT BUỘC REPORT**

Sau mỗi Sprint xuất file markdown.

Format:

**Sprint X Report**

**Objective**

Mục tiêu Sprint.![ref7]

**Files Created**

- file1.py
- file2.py![ref6]

**Files Modified**

- file3.py![ref8]

**Functions Implemented**

**function\_name()**

Mô tả.![](Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.010.png)

**API Added**

GET /...

POST /...![](Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.011.png)

**Testing**

Các test đã chạy.![](Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.012.png)

**Result**

PASS / FAIL![ref2]

**Next Sprint Recommendation**

Đề xuất bước tiếp theo.![ref9]

**ROADMAP**

Toàn bộ dự án chia thành các Sprint nhỏ.

Mỗi Sprint tối đa 1-2 giờ code.![ref10]

**SPRINT 1**

Mục tiêu:

Khởi tạo project.

Tạo cấu trúc thư mục.

Tạo FastAPI server.

Tạo file config.

Tạo logger.

Không viết business logic.![ref6]

Output:

backend/

main.py

api.py

config/settings.py

utils/logger.py![ref8]

Kết thúc Sprint:\
Tạo

reports/sprint\_1\_report.md

Dừng.

Chờ xác nhận.![ref6]

**SPRINT 2**

Mục tiêu:

Tạo schema.![ref7]

Tạo:

schemas/

angle.py

caption.py

image.py

evaluation.py

draft.py![ref4]

Dùng Pydantic.\
Kết thúc:![ref8]

reports/sprint\_2\_report.md

Dừng.![ref6]

**SPRINT 3**

Mục tiêu:

Tạo Storage Layer.![ref7]

Tạo:

storage/

drafts/

images/

logs/

outputs/![ref1]

Tạo:

file\_utils.py

json\_utils.py![ref7]

Functions:

save\_json()

load\_json()

save\_draft()

load\_draft()![ref4]

Tạo:

reports/sprint\_3\_report.md

Dừng.![ref8]

**SPRINT 4**

Mục tiêu:

Knowledge Module.![ref1]

Files:

knowledge/

dify\_client.py

search.py

insight\_extractor.py![ref7]

Functions:

search\_dataset()

retrieve\_chunks()

extract\_insights()![ref1]

Không tạo UI.

Không tạo workflow.\
Tạo:![ref6]

reports/sprint\_4\_report.md

Dừng.![ref5]

**SPRINT 5**

Mục tiêu:

Angle Module.![ref9]

Files:

angle/

angle\_generator.py

angle\_selector.py![ref7]

Functions:

generate\_angles()

select\_best\_angle()![ref9]

Output:

3 angles.![ref7]

Tạo report.

Dừng.![ref1]

7
**SPRINT **9****

Mục tiêu:

Caption Module.![ref1]

Files:

caption/

caption\_generator.py

hashtag\_generator.py

thread\_generator.py![ref7]

Functions:

generate\_caption()

generate\_hashtags()

generate\_thread()![ref1]

Output:

Instagram Caption

Threads Caption

Hashtags![ref11]

Tạo report.

Dừng.![ref9]

Mục tiêu:

Caption Evaluation.![ref1]

Files:

evaluation/

caption\_evaluator.py

retry\_caption.py![ref11]

Functions:

evaluate\_caption()

improve\_caption()![ref1]

Criteria:

Hook

Emotion

Insight

CTA

Clarity![ref11]

Pass Threshold:

8\.0![ref9]

Tạo report.

Dừng.

9

**SPRINT 8![ref4]**

Mục tiêu:

Image Module.![ref11]

Files:

image/

prompt\_builder.py

image\_generator.py

image\_store.py![ref1]

Functions:

build\_prompt()

generate\_image()

save\_image()![ref11]

Tạo report.

Dừng.![ref9]

**SPRINT 9**

Mục tiêu:

Image Evaluation.![ref10]

Files:

evaluation/

10

image\_evaluator.py

retry\_image.py![ref4]

Functions:

evaluate\_image()

improve\_image()![ref8]

Criteria:

Character

Composition

Color

Style![ref6]

Tạo report.

Dừng.![ref8]

**SPRINT 10**

Mục tiêu:

Pipeline Orchestrator.![ref1]

File:

orchestrator/pipeline.py![ref11]

Flow:

Knowledge

↓

Angle

↓

Caption

↓

Caption Evaluation

↓

Image

↓

Image Evaluation

↓

Draft![ref9]

Function:

run\_pipeline()![ref7]

Tạo report.

Dừng.![ref1]

**SPRINT 11**

Mục tiêu:

Markdown Export.![ref2]

Files:

publish/

markdown\_exporter.py![ref4]

Function:

export\_markdown()![ref5]

Output:

draft.md![ref6]

Tạo report.

Dừng.![ref8]

**SPRINT 12**

Mục tiêu:

Review API.![ref1]

Endpoints:

GET /drafts

POST /approve

POST /reject

POST /rerun![ref7]

Tạo report.

Dừng.![ref1]

13
**SPRINT **14****

Mục tiêu:

Instagram Publish.![ref1]

Files:

publish/

instagram\_client.py![ref7]

Function:

publish\_instagram()![ref1]

Tạo report.

Dừng.![ref11]

**SPRINT 14**

Mục tiêu:

Threads Publish.![ref3]

Files:

publish/

threads\_client.py![ref2]

Function:

publish\_threads()![ref3]

14

Tạo report.

Dừng.![ref4]

**SPRINT 15**

Mục tiêu:

End-to-End Test.![ref11]

Chạy:

Input

↓

Knowledge

↓

Angle

↓

Caption

↓

Image

↓

Markdown![ref5]

Tạo:

reports/final\_report.md![ref6]

Dừng hoàn toàn.

15

Không tự ý thêm chức năng mới.
16

[ref1]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.001.png
[ref2]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.002.png
[ref3]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.003.png
[ref4]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.004.png
[ref5]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.005.png
[ref6]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.007.png
[ref7]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.008.png
[ref8]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.009.png
[ref9]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.013.png
[ref10]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.014.png
[ref11]: Aspose.Words.611c2d13-28a5-487f-a80e-67eb94adcb51.015.png
