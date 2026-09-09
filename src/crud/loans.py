from sqlalchemy.orm import Session
from..models import Loan, Client
from..schemas.loan import LoanCreate, Loan

def create_loan(db: Session, loan: LoanCreate):
    db_loan = Loan(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

def get_loan(db: Session, loan_id: int):
    return db.query(Loan).filter(Loan.id == loan_id).first()

def update_loan(db: Session, loan_id: int, loan: LoanCreate):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is not None:
        for key, value in loan.dict().items():
            setattr(db_loan, key, value)
        db.commit()
        db.refresh(db_loan)
    return db_loan

def delete_loan(db: Session, loan_id: int):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is not None:
        db.delete(db_loan)
        db.commit()