from exception import StoryException
from fastapi import FastAPI
from router import blog_get, blog_post, user, article
from db.database import engine, Base
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi import Request, HTTPException

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(content={'detail': exc.name}, status_code=418)


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)
