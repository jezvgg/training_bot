from DB.Tables import BaseTable
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey


class UserTable(BaseTable):
    __tablename__ = "users"

    telegram_id = Column("telegram_id", Integer, unique=True, primary_key=True)
    subscribed = Column("subscribed", Boolean, nullable=False)
    username = Column("username", String)
    current_message = Column("current_message", Integer, ForeignKey("dialogue.id"), nullable=False)
    is_accepted = Column("is_accepted", Boolean, nullable=False)
    is_use = Column("is_use", Boolean, nullable=False)


    def __init__(self, id: int, subs: bool, current_message: int, 
                is_accepted: bool, is_use: bool, username: str = None):
        self.telegram_id = id
        self.subscribed = subs
        self.current_message = current_message
        self.is_accepted = is_accepted
        self.is_use = is_use
        self.username = username
    