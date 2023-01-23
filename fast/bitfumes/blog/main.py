from fastapi import FastAPI
from db import models
from db.config import engine
from routers import blog, user, authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
