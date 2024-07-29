from app.db import database
from bson import ObjectId

collection = database["items"]

async def get_document(doc_id: str):
    try:
        object_id = ObjectId(doc_id)
        document = await collection.find_one({"_id": object_id})
        # Convert ObjectId to str for serialization
        if document:
            document['_id'] = str(document['_id'])
        return document
    except Exception as e:
        return {"error": str(e)}

# Function to fetch all documents
async def get_documents():
    try:
        documents = await collection.find({}).to_list(None)
        # Convert ObjectId to str for serialization
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return documents
    except Exception as e:
        return {"error": str(e)}
    
async def insert_document(name: str, description: str):
    try:
        result = await collection.insert_one({"name":name, "description":description})
        return {"inserted_id": str(result.inserted_id)} 
    except Exception as e:
        return {"error": str(e)}

async def update_document(doc_id: str, name: str, description: str):
    try:
        object_id = ObjectId(doc_id)
        result = await collection.update_one({"_id":object_id},{"$set": {"name":name, "description":description}})
        if result.matched_count:
            return await get_document()
        return None
    except Exception as e:
        return {"error": str(e)}
    
async def delete_document(doc_id: str):
    try:
        object_id = ObjectId(doc_id)
        result = await collection.delete_one({"_id":object_id})
        if result.deleted_count == 1:
            return {"success": True, "message": f"Document with _id {doc_id} deleted successfully."}
        else:
            return {"success": False, "message": f"Document with _id {doc_id} not found."}

    except Exception as e:
        return {"error": str(e)}
    
