from mongoengine import Document, fields

class ItemModel(Document):
    name = fields.StringField(required=True)
    description = fields.StringField(required=True)

    def to_dict(self):
        return {
            "id": str(self.id),  # Convert ObjectId to string
            "name": self.name,
            "description": self.description
        }