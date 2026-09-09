from sqlalchemy.orm import Session
from..models import Client
from..schemas.client import ClientCreate, Client

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, client: ClientCreate):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is not None:
        for key, value in client.dict().items():
            setattr(db_client, key, value)
        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is not None:
        db.delete(db_client)
        db.commit()