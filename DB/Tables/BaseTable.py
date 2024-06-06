from DB.Tables import Base
from abc import abstractclassmethod


class BaseTable(Base):
    __abstract__ = True


    @abstractclassmethod
    @staticmethod
    def build(model):
        '''
        Фабричный метод создания таблицы из модели
        '''
        pass


    def __repr__(self):
        classname = str(self.__class__)
        fields = [f"{str(field)}={str(getattr(self, field))}" for field in dir(self) if not field.startswith('_')]
        return f"{classname}({', '.join(fields)})"