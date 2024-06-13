from DB.Tables import *
from Src.Models import *


class table_factory:
    '''
    Фабрика для конвертации моделей в таблицы БД.
    '''
    # К какой модели какую таблицу нужно использовать
    __map: dict[AbstractModel, BaseTable] = {
        Keyboard: KeyboardsTable,
        User: UserTable,
        Message: DialogueTable,
        Command: CommandsTable
    }


    @classmethod
    def get(cls, model: AbstractModel):
        '''
        Получить класс таблицы соответсвющий моделе
        '''
        if model not in cls.__map.keys():
            raise Exception('Конвертация модели невозможна. Нет подходящей таблицы в фабрике.')

        if isinstance(model, type(AbstractModel)):
            return cls.__map[model]

        return cls.__map[type(model)]


    @classmethod
    def create(cls, model: AbstractModel) -> BaseTable:
        '''
        Получить таблицу соответсвующую моделе
        '''
        # У этих таблиц соответственно должен быть фабричный метод от модели
        return cls.get(model).build(model)


    @classmethod
    def keys(cls):
        return list(cls.__map.keys())
