from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from schemas import BlogSchema, ShowBlog
from db import crud_blog
from db.config import get_db


def get_all(db: Session):
    blogs = crud_blog.get_blogs(db)
    return blogs
