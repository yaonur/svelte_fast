from fastapi import APIRouter, status, Response, Query, Path, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]

    # class Config:
    #     orm_mode = True


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'id': id, 'data': blog, 'version': version}


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int,
                   comment_id: int = Query(None,
                                           title="id of the comment",
                                           description="Some description for comment_id",
                                           alias='commentID',
                                           deprecated=True
                                           ),
                   # content: str = Body("hey how is it going"),
                   content: str = Body(...,
                                       min_length=5,
                                       max_length=50,
                                       regex='^[a-z\s]*$'
                                       )
                   ):
    return {
        'blog': blog, 'id': id, 'comment_id': comment_id, "content": content
    }
