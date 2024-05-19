from dotenv import dotenv_values
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))

db=client.sample_mflix
collection_cars=db["carsV2"]

collection_users=db["users"]