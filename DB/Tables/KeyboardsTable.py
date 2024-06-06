from DB.Tables import BaseTable
from sqlalchemy import Column, Integer, JSON


class KeyboardsTable(BaseTable):
    __tablename__ = 'keyboards'

    id = Column("id", Integer, unique=True, primary_key=True)
    _data = Column("data", JSON)


    def __init__(self, id: int, data: dict):
        self.id = id
        self._data = data
