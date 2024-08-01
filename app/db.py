import os
from dotenv import load_dotenv
from mongoengine import connect

# Load environment variables from .env file
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "test_db")

def initialize_db():
    connect(
        db=DATABASE_NAME,
        host=MONGODB_URL
    )