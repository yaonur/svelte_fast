from fastapi import FastAPI
from db.model import PostSchema

posts = [
    {
        "id": 1,
        "title": "penguins",
        "text": "Penguining all the day"
    },
    {
        "id": 2,
        "title": "tigers",
        "text": "dont turn your back"
    }
]

users = []

app = FastAPI()


@app.get('/', tags=["test"])
def greet():
    return "hey there"


# Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}


# Get single post {id}
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {"error": "Wrong id"}
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }
