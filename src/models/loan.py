from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    interest_rate = Column(Float, index=True)
    duration = Column(Integer, index=True)
    status = Column(String, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Client', back_populates='loans')