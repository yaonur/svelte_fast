from sqlalchemy.orm.session import Session
from schemas import UserBaseSchema
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBaseSchema):
    new_user = DbUser(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, user_name: str):
    user = db.query(DbUser).filter(DbUser.username == user_name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {user_name} not found')
    return user


def update_user(db: Session, user_name: str, request: UserBaseSchema):
    user = db.query(DbUser).filter(DbUser.username == user_name)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {user_name} not found')
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(db: Session, user_name):
    user = db.query(DbUser).filter(DbUser.username == user_name)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {user_name} not found')

    user.delete()
    db.commit()
    return 'ok'
