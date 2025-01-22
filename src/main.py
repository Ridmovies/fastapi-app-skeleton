from fastapi import FastAPI

from src.dev.router import router as dev_router
from src.posts.router import router as post_router

app = FastAPI()
app.include_router(dev_router, prefix='/dev', tags=['dev'])
app.include_router(post_router, prefix='/posts', tags=['posts'])
