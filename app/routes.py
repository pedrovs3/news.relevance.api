from fastapi import APIRouter, HTTPException
from .models import RankRequest, RankedArticle
from .utils import rank_news
from typing import List

router = APIRouter()


@router.post("/rank", response_model=List[RankedArticle])
def rank_news_endpoint(request: RankRequest):
    """
    Endpoint para classificar notícias por relevância.
    """
    if not request.user_keywords or not request.news:
        raise HTTPException(status_code=400, detail="Palavras-chave e notícias são obrigatórias.")

    ranked_news = rank_news(
        user_keywords=request.user_keywords,
        news=[article.dict() for article in request.news]
    )
    return ranked_news
