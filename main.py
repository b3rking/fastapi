from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Welcome to my api!"}

@app.get('/posts')
def posts():
    return {"data": "this is a list of posts!"}


