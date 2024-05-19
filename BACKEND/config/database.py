from dotenv import dotenv_values
from pymongo import MongoClient


config = dotenv_values(".env")
client = MongoClient(config["MONGODB_URI"])

db=client.sample_mflix
collection_cars=db["carsV2"]

collection_users=db["users"]