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

def test_create_client():
    response = client.post('/clients/', json={'name': 'John Doe', 'age': 30, 'credit_history': 750})
    assert response.status_code == 200

def test_read_client():
    response = client.get('/clients/1')
    assert response.status_code == 200

def test_update_client():
    response = client.put('/clients/1', json={'name': 'Jane Doe', 'age': 35, 'credit_history': 800})
    assert response.status_code == 200

def test_delete_client():
    response = client.delete('/clients/1')
    assert response.status_code == 200