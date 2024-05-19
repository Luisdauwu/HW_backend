from pydantic import BaseModel

class user(BaseModel):
    username: str
    password: str
   