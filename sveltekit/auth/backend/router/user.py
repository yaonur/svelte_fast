from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
import schemas
from auth.oauth2 import get_current_user
from db import crud_user, database, hash
from auth import oauth2

router = APIRouter(prefix="/user", tags=["users"])


@router.get("/all", response_model=list[schemas.UserResponseSchema])
def get_all(db: Session = Depends(database.get_db)):
    users: [schemas.UserBaseSchema] = crud_user.get_all_users(db)
    return users


@router.post('/', response_model=schemas.UserResponseSchema)
def create_user(user: schemas.UserBaseSchema, db: Session = Depends(database.get_db)):
    print(user)
    user: schemas.UserBaseSchema = crud_user.create_user(db=db, request=user)
    return user


@router.post('/login')
def login_user(req: schemas.UserBaseSchema, db: Session = Depends(database.get_db)):
    user: schemas.UserBaseSchema = crud_user.get_user(db=db, username=req.username)
    if not user:
        return False
    if hash.Hash.verify(user.password, req.password):
        token = oauth2.create_access_token(data={'sub': user.username})
    return token


@router.get('/')
def get_user(db: Session = Depends(database.get_db),
             current_user: schemas.UserResponseSchema = Depends(get_current_user)):
    user: schemas.UserBaseSchema = crud_user.get_user(db, current_user['username'])
    return current_user
