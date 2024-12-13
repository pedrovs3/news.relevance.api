from pydantic import BaseModel, Field
from typing import List


class NewsArticle(BaseModel):
    title: str = Field(..., min_length=5, max_length=200)
    content: str = Field(..., min_length=10, max_length=5000)


class RankRequest(BaseModel):
    user_keywords: List[str] = Field(..., min_items=1)
    news: List[NewsArticle] = Field(..., min_items=1)


class RankedArticle(NewsArticle):
    relevance: float = Field(..., ge=0, le=1)
