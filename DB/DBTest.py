from DB.DBInterface import DBInterface
from Src.Models import AbstractModel


class DBTest(DBInterface):
    '''
    МОК для тестирования с БД
    '''
    __map: dict[type: list[AbstractModel]]
    
    def __init__(self, *args: list[AbstractModel]):
        self.__map = {}
        for arg in args:
            if type(arg) not in self.__map.keys():
                self.__map[type(arg)] = [arg]
            else: self.__map[type(arg)] += [arg]


    def __get_type(self, model):
        if isinstance(model, type(AbstractModel)):
            return model

        return type(model)


    def get(self, model: AbstractModel) -> list[AbstractModel]:
        return self.__map[self.__get_type(model)]


    def get_one(self, model: AbstractModel, id: int) -> AbstractModel:
        return self.get_ones(model, id)[0]


    def get_ones(self, model: AbstractModel, id: int) -> list[AbstractModel]:
        return [value for value in self.get(model) if value.id == id]


    def add(self, model: AbstractModel) -> bool:
        if type(model) not in self.__map.keys():
            self.__map[type(model)] = [model]
        else: self.__map[type(model)] += [model]

        return True



