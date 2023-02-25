from sqlalchemy.orm import Session
from model.userModel import User


def create_user(db:Session,user:User)->bool:
    try:
        db.add(user)
        db.commit()
    except:
        return False
    return True

def get_user(db:Session):
    return db.query(User).all()

def get_user_by_username(db:Session,username:str):
    return db.query(User).filter(User.username==username).first()