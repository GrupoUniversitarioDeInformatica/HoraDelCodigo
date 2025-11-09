from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=list[schemas.PostOut])
def list_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@router.get("/{post_id}", response_model=schemas.PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).get(post_id)
    if not post:
        raise HTTPException(404, "Post not found")
    return post


@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
def create_post(payload: schemas.PostCreate, db: Session = Depends(get_db)):
    # Verificar que el usuario exista (buena práctica para el taller)
    user = db.query(models.User).get(payload.user_id)
    if not user:
        raise HTTPException(400, "User does not exist")

    post = models.Post(
        user_id=payload.user_id,
        title=payload.title,
        body=payload.body,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.put("/{post_id}", response_model=schemas.PostOut)
def update_post(post_id: int, payload: schemas.PostUpdate, db: Session = Depends(get_db)):
    post = db.query(models.Post).get(post_id)
    if not post:
        raise HTTPException(404, "Post not found")

    if payload.title is not None:
        post.title = payload.title
    if payload.body is not None:
        post.body = payload.body

    db.commit()
    db.refresh(post)
    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).get(post_id)
    if not post:
        raise HTTPException(404, "Post not found")
    db.delete(post)
    db.commit()
