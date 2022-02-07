from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class CommentBase(BaseModel):
    message: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    post_id: int
    message: str
    time: Optional[datetime] = None

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    title: str
    content: str
    time: Optional[datetime]
    comments: list[Comment] = []

    class Config:
        orm_mode = True
