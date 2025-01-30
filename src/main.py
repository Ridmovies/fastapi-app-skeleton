from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqladmin import Admin

from src.admin.views import PostAdmin
from src.database import engine
from src.dev.router import router as dev_router
from src.posts.router import router as post_router
from src.auth.router import auth_router
from src.users.router import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    yield


app = FastAPI(lifespan=lifespan)
admin = Admin(app, engine)
admin.add_view(PostAdmin)

app.include_router(dev_router, prefix="/dev", tags=["dev"])
app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
