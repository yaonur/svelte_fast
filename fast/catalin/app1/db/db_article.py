from db import models
import schemas
from sqlalchemy.orm.session import Session


def create_article(db: Session, request: schemas.ArticleBaseSchema):
    new_article = models.DbArticle(title=request.title, content=request.content, published=request.published,
                                   user_id=request.creator_id, )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, id: int):
    article = db.query(models.DbArticle).filter(models.DbArticle.id == id).first()
    return article
