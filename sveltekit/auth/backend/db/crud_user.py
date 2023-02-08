from sqlalchemy.orm.session import Session
import schemas
from db.models import DbUser
from db.hash import Hash
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def create_user(db: Session, request: schemas.UserBaseSchema):
    try:
        new_user = DbUser(username=request.username, password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError as err:
        if err.orig.diag.sqlstate == "23505":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="duplicate username")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err.orig.diag.message_detail)
    return new_user


def get_user(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    return user


def get_all_users(db: Session, ):
    users = db.query(DbUser).all()
    return users
