from pydantic import BaseModel, EmailStr, Field, model_validator
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: int = Field(..., le=1)


class PostOut(BaseModel):
    Post: Post
    votes: int

    @model_validator(mode="before")
    @classmethod
    def convert_tuple(cls, values):
        # If the input is a tuple from SQLAlchemy (post_obj, vote_count)
        if isinstance(values, tuple) and len(values) == 2:
            return {"Post": values[0], "votes": values[1]}
        return values

    class Config:
        from_attributes = True
