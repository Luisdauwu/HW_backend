from fastapi import FastAPI
from routes.car_routes import cars_api_router
from routes.user_routes import user_api_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""],
)
app.include_router(cars_api_router)

app.include_router(user_api_router)