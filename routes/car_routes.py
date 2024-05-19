from fastapi import APIRouter, HTTPException
from config.database import collection_cars
from models.cars_models import Cars
from schema.cars_schema import car_serializer, cars_serializer
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

cars_api_router = APIRouter()
load_dotenv()
@cars_api_router.get("/cars", tags=["Cars"])
async def get_cars():
    cars=cars_serializer(collection_cars.find())
    return {"status":"ok","data":cars}

@cars_api_router.get("/cars/{id}", tags=["Cars"])
async def get_car(id:str, access_token:str=None):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        data_user=jwt.decode(access_token, key= os.getenv("ALGORITHM"), algorithms=[os.getenv("ALGORITHM")])
        print(data_user)
        if data_user:
            car=cars_serializer(collection_cars.find({"_id":id}))
            return {"status":"ok","data":car}
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")
    