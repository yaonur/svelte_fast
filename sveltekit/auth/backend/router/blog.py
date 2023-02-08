from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
import schemas
from db import crud_blog, database, hash
from auth import oauth2

router = APIRouter(prefix="/blog", tags=["blogs"])


@router.get("/all", response_model=list[schemas.BlogSchema])
def get_all(db: Session = Depends(database.get_db)):
    blogs: [schemas.BlogSchema] = crud_blog.get_all_blogs(db)
    return blogs


@router.post('/', response_model=schemas.BlogSchema)
def create_blog(blog: schemas.BlogSchema, db: Session = Depends(database.get_db)):
    blog: schemas.BlogSchema = crud_blog.create_blog(db=db, request=blog)
    return blog


@router.post('/login')
def login_user(req: schemas.UserBaseSchema, db: Session = Depends(database.get_db)):
    user: schemas.UserBaseSchema = crud_blog.get_user(db=db, request=req)
    if not user:
        return False
    if hash.Hash.verify(user.password, req.password):
        token=oauth2.create_access_token()


