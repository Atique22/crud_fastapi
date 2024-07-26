from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "test_db")

client = AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]