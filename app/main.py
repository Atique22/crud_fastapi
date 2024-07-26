import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import crud, schemas
from app.db import database

app = FastAPI()

@app.post("/items/", response_model = schemas.Item)
async def create_item(item: schemas.ItemCreate):
    create_item = await crud.create_item(item.name, item.description)
    return create_item

@app.get("/items/{item_id}", response_model = schemas.Item)
async def get_item(item_id: str):
    get_item = await crud.get_item(item_id)
    if get_item is None: 
        raise HTTPException(status_code=404, detail="Item not found")
    return get_item

@app.put("/items/{item_id}", response_model=schemas.Item)
async def update_item(item_id: str, item: schemas.ItemCreate):
    updated_item = await crud.update_item(item_id, item.name, item.description)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    success = await crud.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)