import uvicorn
from fastapi import FastAPI, HTTPException
from app import crud

app = FastAPI()

@app.get("/items")
async def get_items():
    try:
        return await crud.get_documents()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/items/{item_id}/")
async def get_item(doc_id: str):
    try:
        return await crud.get_document(doc_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/items/")
async def create_new_item(name: str, decription: str):
    try:
        return await crud.insert_document(name = name, description= decription)   
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.put("/items/{item_id}/")
async def update_new_item(doc_id: str, name: str, decription: str):
    try:
        return await crud.update_document(doc_id = doc_id, name = name, description= decription)   
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.delete("/items/{item_id}/")
async def delete_item(doc_id: str):
    try:
        return await crud.delete_document(doc_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))