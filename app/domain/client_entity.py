from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = 'client'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    client_name = Column(String(100), nullable=False)
    client_address = Column(String(500))
