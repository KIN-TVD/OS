import uuid
import os
from datetime import datetime
from typing import Optional
from src.utils.logger import logger
from src.schemas.draft import Draft

from src.knowledge.insight_extractor import extract_insights
from src.angle.angle_generator import generate_angles, select_best_angle
from src.caption.caption_generator import generate_caption
from src.caption.thread_generator import generate_thread
from src.caption.hashtag_generator import generate_hashtags
from src.evaluation import evaluate_caption, improve_caption, evaluate_image, improve_image
from src.image import build_prompt, generate_image, save_image
from src.storage.json_utils import save_json

def run_pipeline(topic: str, platform: str = "instagram") -> Draft:
    logger.info(f"--- STARTING PIPELINE FOR TOPIC: '{topic}' | PLATFORM: '{platform}' ---")
    draft_id = f"draft_{uuid.uuid4().hex[:8]}"

    # Fallback to topic as context directly if we skip dify knowledge retrieval for simplicity
    context_text = topic 
    
    # 1. Insight Phase
    logger.info("[PHASE 1] Extracting Insights...")
    insights = extract_insights(context_text)
    
    # 2. Angle Phase
    logger.info("[PHASE 2] Generating Angles...")
    angles = generate_angles(insights, topic)
    best_angle = select_best_angle(angles) if angles else None

    # 3. Caption Phase
    logger.info("[PHASE 3] Generating Caption...")
    if platform.lower() == "threads":
        caption = generate_thread(best_angle)
    else:
        caption = generate_caption(best_angle, platform)
        hashtags = generate_hashtags(caption.text, topic)
        if hashtags:
            caption.text += "\n\n" + " ".join(hashtags)

    # 4. Caption Evaluation Phase
    logger.info("[PHASE 4] Evaluating Caption...")
    cap_eval = evaluate_caption(caption)
    if cap_eval.overall_score < 8.0:
        logger.info("Caption score < 8.0. Triggering improvement...")
        caption = improve_caption(caption, cap_eval)

    # 5. Image Phase
    logger.info("[PHASE 5] Translating Caption to Image Prompt...")
    img_prompt = build_prompt(caption)
    
    logger.info("[PHASE 6] Generating Image...")
    image_obj = generate_image(img_prompt)

    # 6. Image Evaluation Phase
    img_eval = None
    if image_obj.base64_data:
        logger.info("[PHASE 7] Evaluating Image...")
        img_eval = evaluate_image(image_obj)
        if img_eval.overall_score < 8.0:
            logger.info("Image score < 8.0. Triggering improvement...")
            image_obj = improve_image(image_obj, img_eval)

        logger.info("Saving physical image file...")
        save_image(image_obj)

    # 7. Draft Generation Phase
    logger.info("[PHASE 8] Assembling Final Draft...")
    draft = Draft(
        id=draft_id,
        title=f"Draft for {topic}",
        angle=best_angle,
        captions=[caption],
        image=image_obj,
        caption_evaluation=cap_eval,
        image_evaluation=img_eval
    )

    draft_path = os.path.join("data", "drafts", f"{draft_id}.json")
    save_json(draft_path, draft.model_dump(mode="json"))
    logger.info(f"Pipeline completed! Draft saved at {draft_path}")

    return draft
