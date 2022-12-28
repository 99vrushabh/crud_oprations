from pydantic import BaseModel
from server.utils.database import Base
from sqlalchemy import String, Boolean, Integer, Column, DateTime


class payment(BaseModel): 
    id: int
    name: str
    status: bool
    date_birth: str

    class Config:
        orm_mode = True


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
    status = Column(Boolean, default=False)
    date_birth = Column(DateTime)
