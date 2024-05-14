from sqlalchemy import Column, INTEGER, String, DateTime
from sqlalchemy.sql import func
from database.db import Base

class Pokemon(Base):
    __tablename__  = 'pokemons_teste2'
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now()) # Campo adicionado

