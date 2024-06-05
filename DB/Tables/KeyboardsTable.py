from DB.Tables import Base
from sqlalchemy import Column, Integer, JSON


class KeyboardsTable(Base):
    __tablename__ = 'keyboards'

    id = Column("id", Integer, unique=True, primary_key=True)
    data = Column("data", JSON)


    def __init__(self, id: int, data: dict):
        self.id = id
        self.data = data


    def __repr__(self): return f"Keyboard({self.id})"
