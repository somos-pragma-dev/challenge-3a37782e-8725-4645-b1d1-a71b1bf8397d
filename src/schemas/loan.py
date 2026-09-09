from pydantic import BaseModel
from typing import Optional

class LoanCreate(BaseModel):
    amount: float
    interest_rate: float
    duration: int
    status: str
    client_id: int

class Loan(LoanCreate):
    id: int
    client_id: int

    class Config:
        orm_mode = True