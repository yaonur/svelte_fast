from db import models
import schemas
from sqlalchemy.orm.session import Session
from fastapi import HTTPException,status
from exception import StoryException


def create_article(db: Session, request: schemas.ArticleBaseSchema):
    if request.content.startswith("Once upon a time"):
        raise StoryException("No story plz")
    new_article = models.DbArticle(title=request.title, content=request.content, published=request.published,
                                   user_id=request.creator_id, )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, id: int):
    article = db.query(models.DbArticle).filter(models.DbArticle.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id:{id} not found')

    return article
