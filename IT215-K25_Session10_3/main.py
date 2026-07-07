from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import *
from schemas import *
from models import *
from user_service import *

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/inventories", response_model=InventoryResponse, status_code=status.HTTP_201_CREATED)
def create_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    check = create_inventory(inventory, db)
    if not check:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Mã kho đã tồn tại"
        )
    return check