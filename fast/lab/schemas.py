from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserResponseSchema(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
