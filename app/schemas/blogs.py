from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    content: str
    author: Optional[str] = None

class BlogResponse(Blog):
    id: str
