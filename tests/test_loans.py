from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from..main import app, get_db
from..database import Base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_loan():
    response = client.post('/loans/', json={'amount': 1000, 'interest_rate': 5, 'duration': 12, 'status': 'active', 'client_id': 1})
    assert response.status_code == 200

def test_read_loan():
    response = client.get('/loans/1')
    assert response.status_code == 200

def test_update_loan():
    response = client.put('/loans/1', json={'amount': 1500, 'interest_rate': 6, 'duration': 18, 'status': 'inactive', 'client_id': 1})
    assert response.status_code == 200

def test_delete_loan():
    response = client.delete('/loans/1')
    assert response.status_code == 200