from pydantic import BaseModel

# User Schemas
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# Sweet Schemas
class SweetCreate(BaseModel):
    name: str
    price: float
    quantity: int

class SweetUpdate(BaseModel):
    name: str
    price: float
    quantity: int

class SweetResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
