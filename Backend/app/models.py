from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="USER")  # USER or ADMIN


class Sweet(Base):
    __tablename__ = "sweets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
