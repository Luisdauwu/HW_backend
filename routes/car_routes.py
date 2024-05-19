from fastapi import APIRouter, HTTPException
from config.database import collection_cars
from models.cars_models import Cars
from schema.cars_schema import car_serializer, cars_serializer
from jose import JWTError, jwt
from dotenv import dotenv_values

config = dotenv_values(".env")
cars_api_router = APIRouter()
@cars_api_router.get("/cars")
async def get_cars():
    cars=cars_serializer(collection_cars.find())
    return {"status":"ok","data":cars}

@cars_api_router.get("/cars/{id}")
async def get_car(id:str, access_token:str=None):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        data_user=jwt.decode(access_token, key= config["SECRET_KEY"], algorithms=[config["ALGORITHM"]])
        print(data_user)
        if data_user:
            car=cars_serializer(collection_cars.find({"_id":id}))
            return {"status":"ok","data":car}
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")
    