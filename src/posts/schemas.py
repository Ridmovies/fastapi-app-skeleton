from pydantic import BaseModel


class PostSchema(BaseModel):
    content: str


class PostOutSchema(BaseModel):
    id: int
    content: str

