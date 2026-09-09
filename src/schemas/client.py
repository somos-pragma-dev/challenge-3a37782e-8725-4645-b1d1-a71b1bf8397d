from pydantic import BaseModel
from typing import Optional, List

class ClientCreate(BaseModel):
    name: str
    age: int
    credit_history: float

class Client(ClientCreate):
    id: int
    loans: List[Optional['Loan']] = []

    class Config:
        orm_mode = True