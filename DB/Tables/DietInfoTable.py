from DB.Tables import BaseTable
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, Boolean, Sequence




class DietInfoTable(BaseTable):
    __tablename__ = 'diet_info'

    subscribe_id = Column('id', Integer, unique=True,
                        primary_key=True, nullable=False)
    id = Column("user_id", BigInteger, ForeignKey('users.telegram_id'))
    product = Column("product", String)
    diet_goal = Column("diet_goal", String)
    count_trainings = Column("count_trainigs", String)
    diet= Column("diet", String)
   


    def __init__(self,  id: int, product: str = None, diet_goal: str = None, count_trainigs: str = None):
        self.id = id
        self.product = product
        self.diet_goal = diet_goal
        self.count_trainings = count_trainigs
