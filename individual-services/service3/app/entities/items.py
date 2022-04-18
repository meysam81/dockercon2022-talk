from datetime import datetime

from .base import BaseModel


class Items(BaseModel):
    id: int
    name: str
    description: str
    price: float
    tax: float
    created_at: datetime
    updated_at: datetime


class CreateItem(BaseModel):
    name: str
    description: str
    price: float
    tax: float


class UpdateItem(BaseModel):
    name: str
    description: str
    price: float
    tax: float
