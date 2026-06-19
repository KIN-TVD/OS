from pydantic import BaseModel, Field
from typing import Optional

class Angle(BaseModel):
    id: str = Field(..., description="Unique identifier for the angle")
    title: str = Field(..., description="Title of the creative angle")
    description: str = Field(..., description="Detailed description of the angle")
    confidence_score: Optional[float] = Field(default=None, description="Confidence score of this angle")
