from fastapi import FastAPI
from db.database import Base, engine
from router import user,blog
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication

origins = [
    "*"
    # "http://localhost:5173",
    # "http://locahost"
    # "http://localhost:8080",
]
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(authentication.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)