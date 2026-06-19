from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from src.schemas.angle import Angle
from src.schemas.caption import Caption
from src.schemas.image import Image
from src.schemas.evaluation import CaptionEvaluation, ImageEvaluation

class Draft(BaseModel):
    id: str = Field(..., description="Draft unique identifier")
    title: str = Field(..., description="Title or name of the draft")
    status: str = Field(default="pending", description="Draft status (e.g., pending, approved, rejected)")
    published_platforms: List[str] = Field(default_factory=list, description="Danh sách các nền tảng đã publish")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    
    angle: Optional[Angle] = None
    captions: List[Caption] = Field(default_factory=list, description="List of generated captions")
    image: Optional[Image] = None
    
    caption_evaluation: Optional[CaptionEvaluation] = None
    image_evaluation: Optional[ImageEvaluation] = None
