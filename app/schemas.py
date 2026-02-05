from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class MedicineBase(BaseModel):
    name: str
    manufacturer: str
    price: Decimal
    quantity: int

class MedicineCreate(MedicineBase):
    pass

class MedicineUpdate(BaseModel):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    price: Optional[Decimal] = None
    quantity: Optional[int] = None

class MedicineResponse(MedicineBase):
    id: int

    class Config:
        from_attributes = True
