from fastapi import FastAPI
from sqlalchemy.orm import Session
from.database import SessionLocal, engine
from.models import Base
from.crud.loans import create_loan, get_loan, update_loan, delete_loan
from.crud.clients import create_client, get_client, update_client, delete_client
from.schemas.loan import LoanCreate, Loan
from.schemas.client import ClientCreate, Client

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/loans/', response_model=Loan)
def create_new_loan(loan: LoanCreate, db: Session = SessionLocal):
    return create_loan(db=db, loan=loan)

@app.get('/loans/{loan_id}', response_model=Loan)
def read_loan(loan_id: int, db: Session = SessionLocal):
    db_loan = get_loan(db=db, loan_id=loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    return db_loan

@app.put('/loans/{loan_id}', response_model=Loan)
def update_existing_loan(loan_id: int, loan: LoanCreate, db: Session = SessionLocal):
    updated_loan = update_loan(db=db, loan_id=loan_id, loan=loan)
    if updated_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    return updated_loan

@app.delete('/loans/{loan_id}')
def delete_existing_loan(loan_id: int, db: Session = SessionLocal):
    deleted_loan = delete_loan(db=db, loan_id=loan_id)
    if deleted_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    return {'detail': 'Loan deleted'}

@app.post('/clients/', response_model=Client)
def create_new_client(client: ClientCreate, db: Session = SessionLocal):
    return create_client(db=db, client=client)

@app.get('/clients/{client_id}', response_model=Client)
def read_client(client_id: int, db: Session = SessionLocal):
    db_client = get_client(db=db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return db_client

@app.put('/clients/{client_id}', response_model=Client)
def update_existing_client(client_id: int, client: ClientCreate, db: Session = SessionLocal):
    updated_client = update_client(db=db, client_id=client_id, client=client)
    if updated_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return updated_client

@app.delete('/clients/{client_id}')
def delete_existing_client(client_id: int, db: Session = SessionLocal):
    deleted_client = delete_client(db=db, client_id=client_id)
    if deleted_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return {'detail': 'Client deleted'}