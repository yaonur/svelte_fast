from typing import Optional
from fastapi import APIRouter, status, Response, Depends
from sqlalchemy.orm import Session
import schemas
from db import db_user, database
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/user', tags=['users'])


@router.post('/create_user', response_model=schemas.UserResponseSchema)
def create_user(user: schemas.UserBaseSchema, db: Session = Depends(database.get_db),
                ):
    user: schemas.UserBaseSchema = db_user.create_user(db=db, request=user)
    return user


@router.get('/', response_model=list[schemas.UserResponseSchema])
def get_all_users(db: Session = Depends(database.get_db),
                  current_user: schemas.UserResponseSchema = Depends(get_current_user)):
    users: list[schemas.UserBaseSchema] = db_user.get_all_users(db=db)
    return users


@router.get('/{user_name}', response_model=schemas.UserResponseSchema)
def get_user(user_name: str, db: Session = Depends(database.get_db),
             current_user: schemas.UserResponseSchema = Depends(get_current_user)):
    user: schemas.UserBaseSchema = db_user.get_user(db, user_name)
    return user


@router.post('/{user_name}/update')
def update_user(user_name: str, request: schemas.UserBaseSchema, db: Session = Depends(database.get_db),
                current_user: schemas.UserResponseSchema = Depends(get_current_user)):
    return db_user.update_user(db, user_name, request)


@router.get('/{user_name/delete')
def update_user(user_name: str, db: Session = Depends(database.get_db),
                current_user: schemas.UserResponseSchema = Depends(get_current_user)):
    return db_user.delete_user(db, user_name)
