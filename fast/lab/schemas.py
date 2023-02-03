from typing import Optional
from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    username: str
    email: Optional[str]
    password: str

    class Config:
        orm_mode = True


class UserResponseSchema(BaseModel):
    username: str
    email: Optional[str]

    class Config:
        orm_mode = True
