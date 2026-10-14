from fastapi import FastAPI
from app.routers import auth, vote, ai
from . import models
from .database import engine
from .routers import post, user
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(
#     bind=engine
# )  # (not needed anymore as now using alembic migration tool, but not required to be removed too)command to tell sqlalchemy to run the create statemen, so that it can generate all the tables if not present already

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

myposts = [{"title": "title1", "content": "content1", "id": 1}]


def find_post(id):
    for p in myposts:
        if p["id"] == id:
            return p


def get_index(id: int):
    for index, post in enumerate(myposts):
        if post["id"] == id:
            return index


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(ai.router)
