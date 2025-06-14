from sqlalchemy import Column, Integer, String
from .config import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    correo = Column(String, index=True)
    password = Column(String, index=True)
