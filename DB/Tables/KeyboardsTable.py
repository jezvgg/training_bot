from DB.Tables import BaseTable
from Src.Models import Keyboard
from sqlalchemy import Column, Integer, JSON


class KeyboardsTable(BaseTable):
    __tablename__ = 'keyboards'

    id = Column("id", Integer, unique=True, primary_key=True)
    _data = Column("data", JSON)


    @staticmethod
    def build(model: Keyboard):
        return KeyboardsTable(model.id, model.data)


    def __init__(self, id: int, data: dict):
        self.id = id
        self._data = data


    def model(self) -> Keyboard:
        return Keyboard(self.id, self._data)
