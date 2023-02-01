from fastapi import FastAPI
from db.database import Base, engine
from router import user

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user.router)
