from DB.Tables import BaseTable
from sqlalchemy import Column, Integer, String


class MessagesTable(BaseTable):
    __tablename__ = 'messages'
    
    id = Column("id", Integer, unique=True, primary_key=True)
    text = Column("text", String, unique=True, nullable=False)


    def __init__(self, id:int, text: str):
        self.id = id
        self.text = text