from typing import Optional
from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserResponseSchema(BaseModel):
    username: str
    id: str
    items: list

    class Config:
        orm_mode = True


class BlogSchema(BaseModel):
    title: str
    user_id: str

    class Config:
        orm_mode = True
