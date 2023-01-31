import os
from fastapi import FastAPI
from router import blog_get, blog_post, user
from db import models
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
