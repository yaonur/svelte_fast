from sqlalchemy.orm.session import Session
from schemas import UserBaseSchema
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: UserBaseSchema):
    new_user = DbUser(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
