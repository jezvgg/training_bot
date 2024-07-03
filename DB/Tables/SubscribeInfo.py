from DB.Tables import BaseTable, DialogueTable
from Src.Models import Subscribe, Message
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, BigInteger, DateTime, Sequence
from sqlalchemy.orm import relationship
from datetime import datetime


class SubscribeInfo(BaseTable):
    __tablename__ = "subscribe_info"
    
    subscribe_id=Column('id', Integer, unique=True,
                        primary_key=True, nullable=False)
    id = Column("telegram_id", BigInteger)
    subscribe_start = Column("subscribing_start", DateTime(timezone=None))
    subscribe_end = Column("subscribing_end", DateTime(timezone=None))
    count_subskribe_day = Column("count_subskribe_day", Integer)
    subscribe_level = Column("subscribing_level", Integer)


    @staticmethod
    def build(model: Subscribe):
        return (model.id, model.subscribe_start, model.subscribe_end, model.count_subskribe_day, model.subscribe_level,)


    def __init__(self, id: int,   subscribe_start: datetime, subscribe_end: datetime,  count_subskribe_day: int, subscribe_level: int=1):
        self.id=id
        self.subscribe_start=subscribe_start
        self.subscribe_end=subscribe_end
        self.count_subskribe_day=count_subskribe_day
        self.subscribe_level=subscribe_level

    def model(self) -> Subscribe:
        kwargs = {'id':self.id,'subscribe_start':self.subscribe_start,'subscribe_end':self.subscribe_end}
        kwargs|={'count_subskribe_day':self.count_subskribe_day, 'subscribe_level':self.subscribe_level}
        return Subscribe(**kwargs)
    