from datetime import datetime
from pydantic import BaseModel, EmailStr


# ---------- USERS ----------

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str  # en producción: hashea antes de guardar


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- POSTS ----------

class PostBase(BaseModel):
    title: str
    body: str


class PostCreate(PostBase):
    user_id: int


class PostUpdate(BaseModel):
    title: str | None = None
    body: str | None = None


class PostOut(PostBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- COMMENTS ----------

class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    post_id: int
    user_id: int


class CommentUpdate(BaseModel):
    content: str | None = None


class CommentOut(CommentBase):
    id: int
    post_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
