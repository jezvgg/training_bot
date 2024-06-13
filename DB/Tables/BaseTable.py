from DB.Tables import Base
from abc import abstractclassmethod


class BaseTable(Base):
    __abstract__ = True
    id: int


    @staticmethod
    def build(model):
        '''
        Фабричный метод создания таблицы из модели
        '''
        pass


    def model():
        '''
        Фабричный метод возращающий модель с данными из таблицы
        '''
        pass


    def __repr__(self):
        classname = str(self.__class__.__name__)
        fields = [f"{str(field)}={str(getattr(self, field))}" for field in vars(self) if not field.startswith('_')]
        return f"{classname}({', '.join(fields)})"