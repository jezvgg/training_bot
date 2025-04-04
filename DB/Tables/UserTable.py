from DB.Tables import BaseTable, DialogueTable
from Src.Models import User, Message
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, BigInteger, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class UserTable(BaseTable):
    __tablename__ = "users"

    id = Column("telegram_id", BigInteger, unique=True, primary_key=True)
    username = Column("username", String)
    current_message = Column("current_message", Integer, ForeignKey(DialogueTable.id), nullable=False)
    is_accepted = Column("is_accepted", Boolean, nullable=False)
    is_use = Column("is_use", Boolean, nullable=False)

    _current_message = relationship("DialogueTable")


    @staticmethod
    def build(model: User):
        return UserTable(model.id, model.current_message.id, model.is_accepted, 
        model.is_use, model.username)


    def __init__(self, id: int, current_message: int, is_accepted: bool, \
        is_use: bool, username: str = None):
        self.id = id
        self.current_message = current_message
        self.is_accepted = is_accepted
        self.is_use = is_use
        self.username = username


    def model(self) -> User:
        kwargs = {'is_use':self.is_use, 'is_accepted':self.is_accepted, 'username':self.username}
        if self._current_message: kwargs |= {'current_message':self._current_message.model()} 
        else: kwargs |= {'current_message':Message.error_message()}
        kwargs |= {'id':self.id}
        return User(**kwargs)
    