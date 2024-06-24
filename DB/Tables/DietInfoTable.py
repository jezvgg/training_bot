from DB.Tables import BaseTable
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, Boolean


class DietInfoTable(BaseTable):
    __tablename__ = 'diet_info'
    
    id = Column("id", BigInteger, ForeignKey('users.telegram_id'), unique=True, primary_key=True)
    product = Column("product", String)
    diet_goal = Column("diet_goal", String)
    count_trainings = Column("count_trainigs", String)
   


    def __init__(self, id: int, product: str = None, diet_goal: str = None, count_trainigs: str = None):
        self.id = id
        self.product = product
        self.diet_goal = diet_goal
        self.count_trainings = count_trainigs
