from DB.Tables import *


class table_factory:
    '''
    Фабрика для конвертации моделей в таблицы БД.
    '''
    # К какой модели какую таблицу нужно использовать
    __map: dict[BaseTable] = {}

    @staticmethod
    def create(self, model):
        # У этих таблиц соответственно должен быть фабричный метод от модели
        return self.__map[model].build(model)
