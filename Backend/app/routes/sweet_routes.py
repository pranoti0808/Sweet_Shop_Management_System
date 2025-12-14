from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import SweetCreate, SweetResponse

router = APIRouter(
    prefix="/api/sweets",
    tags=["Sweets"]
)

# In-memory database
sweets_db = []
sweet_id_counter = 1


# ➕ Add new sweet
@router.post("/")
def add_sweet(sweet: SweetCreate):
    global sweet_id_counter

    new_sweet = {
        "id": sweet_id_counter,
        "name": sweet.name,
        "price": sweet.price,
        "quantity": sweet.quantity
    }

    sweets_db.append(new_sweet)
    sweet_id_counter += 1

    return new_sweet


# 📄 Get all sweets
@router.get("/", response_model=List[SweetResponse])
def get_sweets():
    return sweets_db


# ✏️ Update sweet
@router.put("/{sweet_id}")
def update_sweet(sweet_id: int, updated_sweet: SweetCreate):
    for sweet in sweets_db:
        if sweet["id"] == sweet_id:
            sweet["name"] = updated_sweet.name
            sweet["price"] = updated_sweet.price
            sweet["quantity"] = updated_sweet.quantity
            return {"message": "Sweet updated successfully"}

    raise HTTPException(status_code=404, detail="Sweet not found")


# ❌ Delete sweet
@router.delete("/{sweet_id}")
def delete_sweet(sweet_id: int):
    for sweet in sweets_db:
        if sweet["id"] == sweet_id:
            sweets_db.remove(sweet)
            return {"message": "Sweet deleted successfully"}

    raise HTTPException(status_code=404, detail="Sweet not found")
