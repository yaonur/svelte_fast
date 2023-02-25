import uvicorn
from fastapi import FastAPI
from model import userModel
from database.db import engine

userModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
