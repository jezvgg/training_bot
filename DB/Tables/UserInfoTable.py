from DB.Tables import BaseTable
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, Boolean


class UserInfoTable(BaseTable):
    __tablename__ = 'users_info'
    
    id = Column("id", BigInteger, ForeignKey('users.telegram_id'), unique=True, primary_key=True)
    gender = Column("gender", Boolean)
    username = Column("name", String)
    age = Column("age", Integer)
    city = Column("city", String)
    weight = Column("weight", Integer)
    height = Column("height", Integer)


    def __init__(self, id: int, gender: bool = None, username: str = None, age: int = None,
                city: str = None, weight: int = None, height: int = None):
        self.id = id
        self.gender = gender
        self.username = username
        self.age = age
        self.city = city
        self.weight = weight
        self.height = height


    
