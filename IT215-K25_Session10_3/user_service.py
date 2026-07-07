from models import InventoryModel
from schemas import InventoryCreate
from sqlalchemy.orm import Session

def create_inventory(payload: InventoryCreate, db: Session):
    check = db.query(InventoryModel).filter(InventoryModel.warehouse_code == payload.warehouse_code).first()
    if check:
        return None
    new_inventory = InventoryModel(
        warehouse_code=payload.warehouse_code,
        location=payload.location
    )
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    
    return new_inventory