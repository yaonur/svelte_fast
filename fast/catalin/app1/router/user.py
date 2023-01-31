from typing import Optional
from fastapi import APIRouter, status, Response, Depends
from enum import Enum

from sqlalchemy.orm import Session

import schemas
from db import db_user, database

router = APIRouter(prefix='/user', tags=['users'])


@router.post('/create_user',response_model=schemas.UserResponseSchema)
def create_user(user: schemas.UserBaseSchema, db: Session = Depends(database.get_db)):
    user: schemas.UserBaseSchema = db_user.create_user(db=db, request=user)
    return user
