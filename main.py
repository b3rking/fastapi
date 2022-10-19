from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()

@app.get('/')
def root():
    return {"message": "Welcome to my api!"}

@app.get('/posts')
def posts():
    return {"data": "this is a list of posts!"}

@app.post('/posts')
async def posts(payload: dict = Body()):
    return {"message": "post created!", "data": payload}