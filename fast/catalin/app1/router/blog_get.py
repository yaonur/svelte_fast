from typing import Optional
from router.blog_post import required_functionality
from fastapi import APIRouter, status, Response, Depends
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']

)


@router.get('/all', summary="Retrieve all blogs",
            description="This api call simulates fetching all blogs",
            response_description='The list of available blogs')
def get_blogs(page=1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'message': f"All {page_size} blogs on page {page} "}


@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    '''
    Simulates retrieving a comment of a blog
    :param id: mandatory path parameter
    :param comment_id:  mandatory path paramater
    :param valid: is comment valid
    :param username: the user which comment belongs to
    :return: a comment
    '''
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{b_type}', )
def get_blog_type(b_type: BlogType):
    return {'message': f"Blog type {b_type}"}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f"Blog {id} not found"}
    return {'message': f"Blog with id {id}"}
