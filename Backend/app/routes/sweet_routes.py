from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import SweetCreate, SweetUpdate

router = APIRouter(prefix="/api/sweets", tags=["Sweets"])

# Temporary in-memory database
sweets_db = [
    {"id": 1, "name": "Chocolate", "price": 50.0, "quantity": 100},
    {"id": 2, "name": "Ladoo", "price": 30.0, "quantity": 50}
]

# Get all sweets
@router.get("/", response_model=List[SweetCreate])
def get_sweets():
    return sweets_db

# Add new sweet
@router.post("/")
def add_sweet(sweet: SweetCreate):
    new_id = max([s["id"] for s in sweets_db], default=0) + 1
    new_sweet = {"id": new_id, **sweet.dict()}
    sweets_db.append(new_sweet)
    return {"message": "Sweet added successfully", "sweet": new_sweet}

# Edit sweet
@router.put("/{sweet_id}")
def edit_sweet(sweet_id: int, sweet: SweetUpdate):
    for s in sweets_db:
        if s["id"] == sweet_id:
            s["name"] = sweet.name
            s["price"] = sweet.price
            s["quantity"] = sweet.quantity
            return {"message": "Sweet updated successfully", "sweet": s}
    raise HTTPException(status_code=404, detail="Sweet not found")

# Delete sweet
@router.delete("/{sweet_id}")
def delete_sweet(sweet_id: int):
    for s in sweets_db:
        if s["id"] == sweet_id:
            sweets_db.remove(s)
            return {"message": "Sweet deleted successfully"}
    raise HTTPException(status_code=404, detail="Sweet not found")
