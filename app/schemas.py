from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: Optional[str]
    class Config:
            # Use 'orm_mode' if you're using an ORM, otherwise, you might not need this
            orm_mode = True
