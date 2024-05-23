from fastapi import APIRouter, HTTPException
from config.database import collection_cars
from models.cars_models import Cars
from schema.cars_schema import car_serializer, cars_serializer
from jose import JWTError, jwt
import os
import uuid
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from fastapi import Depends
from bson import ObjectId

cars_api_router = APIRouter()
load_dotenv()

@cars_api_router.get("/cars", tags=["Cars"])
async def get_cars():
    cars = cars_serializer(collection_cars.find())
    return {"status": "ok", "data": cars}

@cars_api_router.get("/cars/{id}", tags=["Cars"])
async def get_car(id: str, access_token: str = None):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        data_user = jwt.decode(access_token, key=os.getenv("ALGORITHM"), algorithms=[os.getenv("ALGORITHM")])
        print(data_user)
        if data_user:
            car = cars_serializer(collection_cars.find({"_id": id}))
            return {"status": "ok", "data": car}
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")

async def get_token(token: str = Depends()):
    return token

@cars_api_router.post("/cars", tags=["Cars"])
async def add_car(car: Cars):
    car_dict = car.dict()
    result = collection_cars.insert_one(car_dict)
    if result.inserted_id:
        return {"status": "ok", "message": "Car added successfully", "car_id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to add car")
    

@cars_api_router.delete("/cars/{car_id}", tags=["Cars"])
async def delete_car(car_id: str):
    try:
        car_object_id = ObjectId(car_id)  # Convertir a ObjectId
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid car ID")
    result = collection_cars.delete_one({"_id": car_object_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"status": "ok", "message": f"Car with ID {car_id} deleted successfully"}
