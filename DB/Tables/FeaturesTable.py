from DB.Tables import BaseTable
from sqlalchemy import Column, Integer, String
from Src.Models import Feature


class FeaturesTable(BaseTable):
    __tablename__ = 'features'

    id = Column("id", Integer, unique=True, primary_key=True)
    text = Column("data", String)


    @classmethod
    def build(cls, model: Feature):
        return FeaturesTable(model.id, model.text)


    def __init__(self, id: int, text: str):
        self.id = id
        self.text = text


    def model(self):
        return Feature(self.id, self.text)
