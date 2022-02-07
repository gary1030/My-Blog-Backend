from datetime import datetime

from sqlalchemy.orm import Session

from fastapi import HTTPException
from . import models, schemas


def get_post(db: Session, post_id: int):
    """get a post"""
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    """get all post (at most 100)"""
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.PostCreate):
    """create a post"""
    date_time_obj = datetime.now()
    db_post = models.Post(
        title=post.title, content=post.content, time=date_time_obj)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_comments_by_post_id(db: Session, post_id: int):
    """get all comments under a post"""
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=400, detail="Post not found")
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()


def create_comment(db: Session, post_id: int, comment: schemas.CommentCreate):
    """create a comment under a post"""
    date_time_obj = datetime.now()
    post = db.query(models.Post).filter(
        models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=400, detail="Post not found")

    db_comment = models.Comment(
        post_id=post_id, message=comment.message, time=date_time_obj)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
