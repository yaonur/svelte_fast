from sqlalchemy.orm.session import Session
import schemas
from db.models import DbBlog
from db.hash import Hash
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def create_blog(db: Session, request: schemas.BlogSchema):
    try:
        new_blog = DbBlog(title=request.title, user_id=request.user_id)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
    except Exception as err:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err)
    return new_blog


def get_user_blogs(db: Session, request: schemas.UserBaseSchema):
    blogs = db.query(DbBlog).filter(DbBlog.user_id == request.user_id)
    return blogs


def get_all_blogs(db: Session, ):
    blog = db.query(DbBlog).all()
    return blog
