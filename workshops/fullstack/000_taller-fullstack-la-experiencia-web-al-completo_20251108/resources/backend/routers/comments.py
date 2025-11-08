from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("/", response_model=list[schemas.CommentOut])
def list_comments(db: Session = Depends(get_db)):
    return db.query(models.Comment).all()


@router.get("/{comment_id}", response_model=schemas.CommentOut)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(models.Comment).get(comment_id)
    if not comment:
        raise HTTPException(404, "Comment not found")
    return comment


@router.post("/", response_model=schemas.CommentOut, status_code=status.HTTP_201_CREATED)
def create_comment(payload: schemas.CommentCreate, db: Session = Depends(get_db)):
    post = db.query(models.Post).get(payload.post_id)
    user = db.query(models.User).get(payload.user_id)

    if not post:
        raise HTTPException(400, "Post does not exist")
    if not user:
        raise HTTPException(400, "User does not exist")

    comment = models.Comment(
        post_id=payload.post_id,
        user_id=payload.user_id,
        content=payload.content,
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


@router.put("/{comment_id}", response_model=schemas.CommentOut)
def update_comment(comment_id: int, payload: schemas.CommentUpdate, db: Session = Depends(get_db)):
    comment = db.query(models.Comment).get(comment_id)
    if not comment:
        raise HTTPException(404, "Comment not found")

    if payload.content is not None:
        comment.content = payload.content

    db.commit()
    db.refresh(comment)
    return comment


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(models.Comment).get(comment_id)
    if not comment:
        raise HTTPException(404, "Comment not found")
    db.delete(comment)
    db.commit()
