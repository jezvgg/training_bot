from DB.Tables import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey


class DialogueTable(Base):
    __tablename__ = 'dialogue'

    id = Column("id", Integer, unique=True, primary_key=True)
    text = Column("text", Integer, ForeignKey("messages.id"), nullable=False)
    keyboard = Column("keyboard", Integer, ForeignKey("keyboards.id"))
    eventname = Column("eventname", String)
    next_message = Column("next_message", Integer, ForeignKey("dialogue.id"), nullable=False)


    def __init__(self, id: int, text: str, next_message: int, keyboard: int = None, eventname: str = None):
        self.id = id
        self.text = text
        self.keyboard = keyboard
        self.eventname = eventname
        self.next_message = next_message


    def __repr__(self):
        return f"Dialogue({self.id}, {self.text}, {self.keyboard}, {self.eventname}, {self.next_message})"

