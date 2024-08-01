import uvicorn
import uuid
from fastapi import FastAPI, HTTPException
from app import crud
from app.schemas import ItemCreateSchema, ItemResponseSchema, ItemUpdateSchema
from app.db import initialize_db
from typing import List


app = FastAPI()
initialize_db()

@app.post("/items/", response_model = ItemResponseSchema)
async def create_new_item(item: ItemCreateSchema):
    try:
        item_data = item.dict()
        created_item = await crud.insert_document(item_data)
        if created_item is None:
            raise HTTPException(status_code=500, detail="Failed to create item.")
        return ItemResponseSchema(**created_item)  
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/items", response_model = List[ItemResponseSchema])
async def get_items():
    try:
        results = await crud.get_documents()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/{item_id}/", response_model = ItemResponseSchema)
async def get_item(item_id: str):
    try:
        result = await crud.get_document(item_id)
        return ItemResponseSchema(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@app.put("/items/{item_id}/", response_model = ItemResponseSchema)
async def update_new_item(item_id: str, item: ItemUpdateSchema):
    try:
        result = await crud.update_document(item_id, item.dict(exclude_unset=True))   
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return ItemResponseSchema(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/items/{item_id}/")
async def delete_item(doc_id: str):
    try:
        result = await crud.delete_document(doc_id)
        if 'error' in result:
            raise HTTPException(status_code=404, detail=result['error'])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
