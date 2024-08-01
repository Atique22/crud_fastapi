from bson import ObjectId

from app.models import ItemModel

async def get_document(doc_id: str):
    try:
        object_id = ObjectId(doc_id)
        document = ItemModel.objects.get(id=object_id)
        if document:
            document = document.to_dict()
        return document
    except Exception as e:
        return {"error": str(e)}

# Function to fetch all documents
async def get_documents():
    try:
        items = ItemModel.objects.all()
        return [item.to_dict() for item in items]
    except Exception as e:
        return {"error": str(e)}
    
async def insert_document(item_data: dict):
    try:
        item = ItemModel(**item_data)
        item.save()
        return item.to_dict()
    except Exception as e:
        return {"error": str(e)}

async def update_document(doc_id: str, update_data: dict):
    try:
        object_id = ObjectId(doc_id)
        item_result = ItemModel.objects.get(id=object_id)
        item_result.update(**update_data)
        update_result = ItemModel.objects.get(id=object_id)
        return update_result.to_dict()
    except Exception as e:
        return {"error": str(e)}
    
async def delete_document(doc_id: str):
    try:
        object_id = ObjectId(doc_id)
        item = ItemModel.objects.get(id=object_id)
        item.delete()
        return {"message": "Item {object_id} deleted successfully"}
    except ItemModel.DoesNotExist:
        return {"error": "Item not found"}   
    except Exception as e:
        return {"error": str(e)}
    
