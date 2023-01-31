from fastapi import APIRouter, status, Response, Query, Path, Body
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1": 'val1'}
    image: Optional[Image] = None

    # class Config:
    #     orm_mode = True


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'id': id, 'data': blog, 'version': version}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                   comment_title: int = Query(None,
                                              title="Title of the comment",
                                              description="Some description for comment title",
                                              alias='commentTitle',
                                              deprecated=True
                                              ),
                   # content: str = Body("hey how is it going"),
                   content: str = Body(...,
                                       min_length=5,
                                       max_length=50,
                                       regex='^[a-z\s]*$'
                                       ),
                   v: Optional[List[str]] = Query(['1,0', '1.1', '1.2']),
                   comment_id: int = Path(None, gt=5, le=10)
                   ):
    return {
        'blog': blog, 'id': id, 'comment_title': comment_title, "content": content, "version": v
    }


def required_functionality():
    return {'message': 'some message'}
