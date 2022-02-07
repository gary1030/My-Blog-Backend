from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Post(Base):
    """post"""
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    time = Column(DateTime)

    comments = relationship("Comment", back_populates="owner")


class Comment(Base):
    """comment"""
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    message = Column(String)
    time = Column(DateTime)

    owner = relationship("Post", back_populates="comments")
