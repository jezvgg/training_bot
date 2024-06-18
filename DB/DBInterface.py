from Src.Models import AbstractModel
from DB.Tables import BaseTable
from Src.settings import settings
from sqlalchemy.orm import Query


class DBInterface(object):
    '''
    Интерфейс класса работающего с базой данных
    '''

    def __init__(self, config: settings) -> None:
        pass

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(type(cls), cls).__new__(cls)
        return cls.instance

    def _get(self, model: AbstractModel) -> Query[BaseTable]:
        '''
        Получить таблицу данных соответствующую модели
        '''
        pass

    def _get_one(self, model: AbstractModel, id: int) -> BaseTable: 
        '''
        Получить данные объекта из БД
        '''
        pass

    def _get_ones(self, model: AbstractModel, id: int) -> list[BaseTable]: 
        '''
        Получить все данные всех обектов совпадающих с моделью
        '''
        pass

    def get(self, model: AbstractModel) -> list[AbstractModel]:
        '''
        Получить модели из таблицы данных соответствующей модели
        '''
        pass

    def get_one(self, model: AbstractModel, id: int) -> AbstractModel:
        '''
        Получить модель из БД
        '''
        pass

    def get_ones(self, model: AbstractModel, id: int) -> list[AbstractModel]:
        '''
        Получить все модели всех обектов совпадающих с моделью
        '''
        pass

    def _add(self, table: BaseTable) -> bool:
        '''
        Добавление значения таблицы в БД
        '''
        pass

    def add(self, model: AbstractModel) -> bool: 
        '''
        Добавление модели в БД
        '''
        pass

    def update(self, model: AbstractModel) -> bool:
        '''
        Обновление данных соотвутсвующих модели в БД
        '''
        pass