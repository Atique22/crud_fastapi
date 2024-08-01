# FastAPI CRUD with MongoDB

This project demonstrates a simple CRUD application using FastAPI and MongoDB. It includes the implementation of API endpoints for creating, reading, updating, and deleting items in a MongoDB database. The project also uses Pydantic schemas for request validation and response serialization.

## Features

- **Create**: Add new items to the database.
- **Read**: Retrieve a list of items or a specific item by ID.
- **Update**: Modify an existing item by ID.
- **Delete**: Remove an item from the database by ID.
- **Testing**: Includes a script to test the CRUD operations.

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- MongoDB
- Pydantic
- MongoEngine (for MongoDB ORM)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Atique22/crud_fastapi.git
   cd crud_fastapi

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt

3. **Set up MongoDB:**
    app/db.py file to point to your MongoDB instance.

4. **Run the FastAPI application:**
    ```bash
    uvicorn app.main:app --reload

5. **Access the API documentation:**

    - Swagger UI: http://127.0.0.1:8000/docs 
    - ReDoc: http://127.0.0.1:8000/redoc

**Endpoints**
- POST /items/: Create a new item.
- GET /items/: Retrieve all items.
- GET /items/{item_id}: Retrieve a specific item by ID.
- PUT /items/{item_id}: Update an existing item by ID.
- DELETE /items/{item_id}: Delete an item by ID.





