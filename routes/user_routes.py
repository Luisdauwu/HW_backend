from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException 
from config.database import collection_users
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from models.user_models import user
from schema.cars_schema import car_serializer, cars_serializer
import uuid
import os
from dotenv import load_dotenv


load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user_api_router = APIRouter()

@user_api_router.post("/auth", tags=["Auth"])
async def login(user:user):
    user_exits = collection_users.find_one({"username":user.username})
    if user_exits:  
        password_verified= verify_password(user.password,user_exits["password"])
        print(password_verified)
        if password_verified:
            token=create_access_token(user_exits)
            return {"status":"ok","token":token}
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrecta!")

@user_api_router.post("/signup", tags=["Auth"])
async def signup(user:user):
    user_exits= collection_users.find_one({"username":user.username})
    if not user_exits:
        password_hashed=get_password_hash(user.password)
        user_db= {
            "_id":uuid.uuid4().hex,
            "username": user.username,
            "password": password_hashed
        }
        collection_users.insert_one(user_db)
        return {"status":"ok"}
    else:
        raise HTTPException(status_code=400, detail="El usuario ya existe!")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt