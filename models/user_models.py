from pydantic import BaseModel
from typing import Optional

class user(BaseModel):
    username: str
    password: str
    role: Optional[str] = None
   