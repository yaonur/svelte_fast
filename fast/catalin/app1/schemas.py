from pydantic import BaseModel


# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserBaseSchema(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    items: list[Article] = []

    class Config:
        orm_mode = True


class ArticleBaseSchema(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

    class Config:
        orm_mode = True


class ArticleResponseSchema(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True
