from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
import schemas
from db import crud_user, database, hash

router = APIRouter(prefix='/user', tags=['user'])


@router.post('/', response_model=schemas.UserResponseSchema)
def create_user(user: schemas.UserBaseSchema, db: Session = Depends(database.get_db)):
    user: schemas.UserBaseSchema = crud_user.create_user(db=db, request=user)
    return user


@router.post('/login')
def login_user(req: schemas.UserBaseSchema, db: Session = Depends(database.get_db)):
    user: schemas.UserBaseSchema = crud_user.get_user(db=db, request=req)
    if not user:
        return False
    return hash.Hash.verify(user.password, req.password)
