from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get('/')
def root():
    return {"message": "Welcome to my api!"}

@app.get('/posts')
def posts():
    return {"data": "this is a list of posts!"}

@app.post('/posts')
async def posts(post: Post):
    return {"message": "post created!", "data": post}