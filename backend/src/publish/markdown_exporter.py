import os
from datetime import datetime
from src.schemas.draft import Draft
from src.utils.logger import logger

OUTPUT_DIR = "data/outputs"

def export_markdown(draft: Draft) -> str:
    """
    Xuất Draft thành file Markdown (.md) trong thư mục data/outputs/.
    Trả về đường dẫn file đã tạo.
    """
    logger.info(f"Exporting draft '{draft.id}' to Markdown...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    lines = []

    # --- Header ---
    lines.append(f"# {draft.title}")
    lines.append(f"")
    lines.append(f"**ID Draft:** `{draft.id}`")
    lines.append(f"**Trạng thái:** `{draft.status}`")
    lines.append(f"**Ngày tạo:** {draft.created_at.strftime('%d/%m/%Y %H:%M') if draft.created_at else 'N/A'}")
    lines.append(f"")
    lines.append("---")
    lines.append("")

    # --- Angle ---
    if draft.angle:
        lines.append("## 📐 Góc Độ Nội Dung")
        lines.append(f"")
        lines.append(f"**Tiêu đề:** {draft.angle.title}")
        lines.append(f"**Mô tả:** {draft.angle.description}")
        lines.append(f"**Điểm Confidence:** {draft.angle.confidence_score:.2f}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # --- Captions ---
    if draft.captions:
        lines.append("## ✍️ Nội Dung Bài Viết")
        lines.append("")
        for cap in draft.captions:
            platform_label = cap.platform.upper() if cap.platform else "ALL"
            lines.append(f"### [{platform_label}]")
            lines.append("")
            lines.append(cap.text)
            lines.append("")
        lines.append("---")
        lines.append("")

    # --- Caption Evaluation ---
    if draft.caption_evaluation:
        ev = draft.caption_evaluation
        lines.append("## 📊 Đánh Giá Caption")
        lines.append("")
        lines.append(f"| Tiêu chí | Điểm |")
        lines.append(f"|----------|------|")
        lines.append(f"| Hook     | {ev.hook_score:.1f} |")
        lines.append(f"| Emotion  | {ev.emotion_score:.1f} |")
        lines.append(f"| Insight  | {ev.insight_score:.1f} |")
        lines.append(f"| CTA      | {ev.cta_score:.1f} |")
        lines.append(f"| Clarity  | {ev.clarity_score:.1f} |")
        lines.append(f"| **Tổng** | **{ev.overall_score:.1f}** |")
        lines.append("")
        if ev.comments:
            lines.append(f"> 💬 **Nhận xét:** {ev.comments}")
        lines.append("")
        passed = "✅ PASS" if ev.overall_score >= 8.0 else "❌ FAIL"
        lines.append(f"**Kết quả:** {passed}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # --- Image ---
    if draft.image:
        lines.append("## 🖼️ Hình Ảnh")
        lines.append("")
        lines.append(f"**Prompt:** {draft.image.prompt}")
        if draft.image.url:
            lines.append(f"**File:** `{draft.image.url}`")
            lines.append("")
            # Nhúng trực tiếp ảnh vào Markdown với URL absolute để Frontend đọc được
            lines.append(f"![Hình Ảnh Sinh Ra](http://localhost:8000{draft.image.url})")
        lines.append("")

        if draft.image_evaluation:
            iev = draft.image_evaluation
            lines.append("### Đánh Giá Hình Ảnh")
            lines.append("")
            lines.append(f"| Tiêu chí    | Điểm |")
            lines.append(f"|-------------|------|")
            lines.append(f"| Character   | {iev.character_score:.1f} |")
            lines.append(f"| Composition | {iev.composition_score:.1f} |")
            lines.append(f"| Color       | {iev.color_score:.1f} |")
            lines.append(f"| Style       | {iev.style_score:.1f} |")
            lines.append(f"| **Tổng**    | **{iev.overall_score:.1f}** |")
            lines.append("")
            if iev.comments:
                lines.append(f"> 💬 **Nhận xét:** {iev.comments}")
            lines.append("")
            passed_img = "✅ PASS" if iev.overall_score >= 8.0 else "❌ FAIL"
            lines.append(f"**Kết quả:** {passed_img}")
            lines.append("")
        lines.append("---")
        lines.append("")

    # --- Footer ---
    lines.append(f"*Được tạo bởi AgentOS Content Studio — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*")

    content = "\n".join(lines)
    filepath = os.path.join(OUTPUT_DIR, f"{draft.id}.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    logger.info(f"Markdown exported successfully: {filepath}")
    return filepath
