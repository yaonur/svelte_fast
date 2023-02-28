from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Request, Response,Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from database.db import get_db
from fastapi.security import OAuth2PasswordRequestForm
from database import userDb
from model.userModel import User
from starlette.responses import RedirectResponse
from auth import auth


class UserForm:
    def __init__(self, username: str=Form(), password: str=Form(),email:str=Form()):
        self.username = username
        self.password = password
        self.email=email

route = APIRouter()
templates = Jinja2Templates(directory="templates/")


@route.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("front/home/index.html", {"request": request})

@route.get("/signin")
def get_login(request: Request):
    return templates.TemplateResponse("auth/signin.html", {"request": request})
@route.get("/signup")
def get_signup(request: Request):
    return templates.TemplateResponse("auth/signup.html", {"request": request})


@route.post("/signup")
def create_new_user(request:Request, db:Session=Depends(get_db),form_data:UserForm=Depends()):
# def create_new_user(request: Request, db: Session = Depends(get_db), ):
    db_user = userDb.get_user_by_username(db=db, username=form_data.username)
    if db_user:
        error = "E-mail already exist"
        return templates.TemplateResponse("auth/signup.html", {"request": request, "error": error}, status_code=301)

    new_user = User(username=form_data.username, email=form_data.username, password=auth.get_password_hash(form_data.password))
    user=userDb.create_user(db=db, user=new_user)
    return templates.TemplateResponse("auth/signin.html", {"request": request,"user":user},status_code=301)

@route.post("/signin",)
def login_for_access_token(response:Response,request:Request, db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = userDb.get_user_by_username(db=db, username=form_data.username)
    if not db_user:
        error = "Invalid credentials"
        return templates.TemplateResponse("auth/signin.html", {"request": request, "error": error}, status_code=301)
    if not auth.verify_password(form_data.password,db_user.password):
        error = "Invalid credentials"
        return templates.TemplateResponse("auth/signin.html", {"request": request, "error": error}, status_code=301)
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(data={"sub": db_user.username}, expires_delta=access_token_expires)
    response=RedirectResponse(url="/",status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", max_age=3600)
    return response

@route.get("/event")
def get_event(request: Request,current_user: User=Depends(auth.get_current_user)):
    print(current_user)
    return templates.TemplateResponse("front/event.html", {"request": request})