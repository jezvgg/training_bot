from DB.Tables import BaseTable, DialogueTable
from Src.Models import User, Message
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship


class UserTable(BaseTable):
    __tablename__ = "users"

    id = Column("telegram_id", BigInteger, unique=True, primary_key=True)
    subscribed = Column("subscribed", Boolean, nullable=False)
    username = Column("username", String)
    current_message = Column("current_message", Integer, ForeignKey(DialogueTable.id), nullable=False)
    is_accepted = Column("is_accepted", Boolean, nullable=False)
    is_use = Column("is_use", Boolean, nullable=False)

    _current_message = relationship("DialogueTable")


    def __init__(self, id: int, subscribed: bool, current_message: int, 
                is_accepted: bool, is_use: bool, username: str = None):
        self.id = id
        self.subscribed = subscribed
        self.current_message = current_message
        self.is_accepted = is_accepted
        self.is_use = is_use
        self.username = username


    def model(self) -> User:
        return self._convert(User, current_message=Message.error_message())
    