import uvicorn
from fastapi import FastAPI
from model import userModel
from database.db import engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import userRoute

userModel.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(userRoute.route, tags=["User"],)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates= Jinja2Templates(directory="templates/")

@app.get("/")
def main():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
