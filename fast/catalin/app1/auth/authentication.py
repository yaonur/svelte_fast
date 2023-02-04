from fastapi import APIRouter, status, Response, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models, hash
from auth import oauth2

router = APIRouter(
    tags=['auth'],
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    if not hash.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail="Invalid password")

    access_token = oauth2.create_access_token(data={'sub': user.username})
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username
    }
