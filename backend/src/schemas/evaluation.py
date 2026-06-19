from pydantic import BaseModel, Field
from typing import Optional

class CaptionEvaluation(BaseModel):
    hook_score: float = Field(..., description="Hook score (e.g., out of 10)")
    emotion_score: float = Field(..., description="Emotion score")
    insight_score: float = Field(..., description="Insight score")
    cta_score: float = Field(..., description="CTA score")
    clarity_score: float = Field(..., description="Clarity score")
    overall_score: float = Field(..., description="Overall average or weighted score")
    comments: Optional[str] = Field(default=None, description="AI reviewer comments")

class ImageEvaluation(BaseModel):
    character_score: float = Field(..., description="Character consistency score")
    composition_score: float = Field(..., description="Composition score")
    color_score: float = Field(..., description="Color matching score")
    style_score: float = Field(..., description="Style alignment score")
    overall_score: float = Field(..., description="Overall average or weighted score")
    comments: Optional[str] = Field(default=None, description="AI reviewer comments")
