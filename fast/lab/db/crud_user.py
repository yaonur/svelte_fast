from sqlalchemy.orm.session import Session
import schemas
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: schemas.UserBaseSchema):
    new_user = DbUser(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, request: schemas.UserBaseSchema):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    return user
