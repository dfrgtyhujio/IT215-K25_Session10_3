from pydantic import BaseModel

class InventoryCreate(BaseModel):
    warehouse_code: str
    location: str

class InventoryResponse(BaseModel):
    id: int
    warehouse_code: str
    location: str

    class Config:
        from_attributes = True