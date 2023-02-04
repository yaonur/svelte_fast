from typing import Optional
from fastapi import APIRouter, status, Response, Depends
from sqlalchemy.orm import Session
import schemas
from db import models, database, db_article
from auth.oauth2 import oauth2_schema, get_current_user
from schemas import UserBaseSchema, UserResponseSchema

router = APIRouter(prefix='/article', tags=['articles'])


@router.post('/', response_model=schemas.ArticleResponseSchema)
def create_article(request: schemas.ArticleBaseSchema, db: Session = Depends(database.get_db),
                   current_user: UserResponseSchema = Depends(get_current_user)):
    return db_article.create_article(db, request)


@router.get('/{id}', )  # response_model=schemas.ArticleResponseSchema)
# def get_article(id: int, db: Session = Depends(database.get_db), token: str = Depends(oauth2_schema)):
def get_article(id: int, db: Session = Depends(database.get_db),
                current_user: UserResponseSchema = Depends(get_current_user)):
    return {
        'data': db_article.get_article(db, id),
        'current_user': current_user
    }
