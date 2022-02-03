from sqlalchemy.orm import Session

from . import models, schemas
from datetime import datetime

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.PostCreate):
    dateTimeObj = datetime.now()
    db_post = models.Post(title=post.title, content=post.content, time=dateTimeObj)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_comments_by_post_id(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()

def create_comment(db: Session, item: schemas.CommentCreate, post_id: int):
    db_comment = models.Comment(**item.dict(), owner_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
