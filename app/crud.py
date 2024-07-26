from app.db import database
from typing import Dict, Any

collection = database["items"]

def convert_objectid_to_str(document):
    if '_id' in document:
        document['id'] = str(document['_id'])
        del document['_id']
    return document

async def create_item(name: str, description: str)-> Dict[str, Any]:
    document = {"name": name, "description": description}
    results = await collection.insert_one(document)
    document["_id"] = str(results.inserted_id)
    return document


async def get_item(item_id: str)-> Dict[str, Any]:
    document = await collection.find_one({"_id":item_id})
    if document:
         return convert_objectid_to_str(document)
    return document


async def update_item(item_id: str, name: str, description: str)-> Dict[str, Any]:
    result = await collection.update_one(
        {"_id": item_id},
        {"$set": {"name": name, "description": description}},
        upsert=False
    )
    if result.matched_count:
        return await get_item(item_id)
    return None

async def delete_item(item_id: str) -> bool:
    result = await collection.delete_one({"_id": item_id})
    return result.deleted_count > 0
