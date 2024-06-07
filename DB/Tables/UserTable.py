from DB.Tables import BaseTable
from Src.Models import User
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey


class UserTable(BaseTable):
    __tablename__ = "users"

    id = Column("telegram_id", Integer, unique=True, primary_key=True)
    subscribed = Column("subscribed", Boolean, nullable=False)
    username = Column("username", String)
    current_message = Column("current_message", Integer, ForeignKey("dialogue.id"), nullable=False)
    is_accepted = Column("is_accepted", Boolean, nullable=False)
    is_use = Column("is_use", Boolean, nullable=False)


    @staticmethod
    def build(model: User):
        return UserTable(model.telegram_id, model.subcribed, model.current_message.id, 
        model.is_accepted, model.is_use, model.username)


    def __init__(self, id: int, subs: bool, current_message: int, 
                is_accepted: bool, is_use: bool, username: str = None):
        self.id = id
        self.subscribed = subs
        self.current_message = current_message
        self.is_accepted = is_accepted
        self.is_use = is_use
        self.username = username


    def model(self, message) -> User:
        message = message.model()
        return User(self.is_use, self.is_accepted, self.username, message, self.subscribed, self.id)
    