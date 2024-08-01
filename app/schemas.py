from pydantic import BaseModel
from typing import Optional


class ItemCreateSchema(BaseModel):
    name: str
    description: str


class ItemUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ItemResponseSchema(BaseModel):
    id: Optional[str]
    name: str
    description: str

    class Config:
        orm_mode = True