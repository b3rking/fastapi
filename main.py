from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

all_posts = [
    {
        "title": "California vibes", 
        "content": "california a pretty town in usa", 
        "id": 1
    },
    {
        "title": "favorite food", 
        "content": "i like chips and meat", 
        "id": 2
    }
]

def find_post(id):
    try:
        for post in all_posts:
            if post['id'] == int(id):
                return post
        return {"error": f"no post found with id {id}"}
    except:
        return {"error": "we encoutered some issue"}


@app.get('/')
def root():
    return {"message": "Welcome to my api!"}

@app.get('/posts')
def posts():
    return {"data": all_posts}

@app.post('/posts')
async def posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    all_posts.append(post_dict)
    return {"message": "post created!", "data": post_dict}

@app.get('/posts/{id}')
def posts(id):
    post = find_post(id)
    return {"data": post}