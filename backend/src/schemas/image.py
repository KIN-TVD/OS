from pydantic import BaseModel, Field
from typing import Optional

class Image(BaseModel):
    id: str = Field(..., description="Unique identifier for the image")
    prompt: str = Field(..., description="The prompt used to generate the image")
    url: Optional[str] = Field(default=None, description="URL of the generated image")
    base64_data: Optional[str] = Field(default=None, description="Base64 encoded image data")
    format: Optional[str] = Field(default=None, description="Image format, e.g., png, jpeg")
