from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username:str
    email:str
    password:str

class Login(BaseModel):
    username: str
    email: str

class TokenData(BaseModel):
    email: Optional[str] = None
