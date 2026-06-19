from pydantic import BaseModel, Field
from typing import List

class Caption(BaseModel):
    id: str = Field(..., description="Unique identifier for the caption")
    platform: str = Field(..., description="Target platform, e.g., Instagram, Threads")
    text: str = Field(..., description="The main content text of the caption")
    hashtags: List[str] = Field(default_factory=list, description="List of hashtags")
