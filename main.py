from typing import Optional
from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from orm import crud, models, schemas
from orm.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

@app.post("/post/")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.get("/posts/")
def get_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db=db)

@app.get("/post/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post(db=db, post_id=post_id)

@app.post("/comment/")
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@app.get("/comment/{comment_id}")
def get_comments_by_post_id(post_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_by_post_id(db=db, post_id=post_id)