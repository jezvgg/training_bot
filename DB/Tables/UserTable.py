from DB.Tables import BaseTable, DialogueTable
from Src.Models import User, Message
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship


class UserTable(BaseTable):
    __tablename__ = "users"

    id = Column("telegram_id", Integer, unique=True, primary_key=True)
    subscribed = Column("subscribed", Boolean, nullable=False)
    username = Column("username", String)
    current_message = Column("current_message", Integer, ForeignKey(DialogueTable.id), nullable=False)
    is_accepted = Column("is_accepted", Boolean, nullable=False)
    is_use = Column("is_use", Boolean, nullable=False)

    _current_message = relationship("DialogueTable")


    @staticmethod
    def build(model: User):
        return UserTable(model.id, model.subcribed, model.current_message.id, 
        model.is_accepted, model.is_use, model.username)


    def __init__(self, id: int, subs: bool, current_message: int, 
                is_accepted: bool, is_use: bool, username: str = None):
        self.id = id
        self.subscribed = subs
        self.current_message = current_message
        self.is_accepted = is_accepted
        self.is_use = is_use
        self.username = username


    def model(self) -> User:
        # LOGGING: Тут должен быть варнинг, что self._current_message пустой
        args = [self.is_use, self.is_accepted, self.username]
        if self._current_message: args += [self._current_message.model(), self.subscribed, self.id]
        else: args += [Message.error_message(),  self.subscribed, self.id]
        return User(*args)
    