from Src.Events import event
from DB.DBInterface import DBInterface
from Src.Models import User
from aiogram import types
from sqlalchemy import Column


class base_save_event(event):
    '''
    Абстрактный Ивент проведения опрос и сохранения данных пользователя
    '''
    _db: DBInterface
    _table_class: type
    _questions: dict[str: str]
    __map: dict[str: str]


    def __init__(self, db: DBInterface):
        self.__map = {}
        self._db = db


    def _start(self, user: User, message: types.Message) -> str:
        table = self._table_class(user.id)
        self._db._add(table)
        return list(self._questions.values())[0]


    def _next(self, user: User, message: types.Message) -> str:
        info = self._db._get_one(self._table_class, user.id)
        for varname in vars(info):
            print(varname)
            if varname.startswith('_') or getattr(info, varname) is not None: continue
            print(varname)
            setattr(info, varname, message.text)

            return self._questions[getattr(getattr(self._table_class, varname), 'name')]


    def _finish(self, user: User, message: types.Message) -> str:
        pass


    def activate(self, user: User, message: types.Message) -> str:
        if not self._db._get_ones(self._table_class, user.id):
            return self._start(user, message)

        return self._next(user, message)


    # @property
    # def questions(self):
    #     return self._questions


    # @questions.setter
    # def questions(self, value: dict[str: str]):
    #     if set(value.keys()) | set(vars(self._table_class).keys()) != set(vars(self._table_class).keys()):
    #         raise Exception('Ключи для ивента сохранения переданы не верно!')

    #     self._questions = value


    # @property
    # def table_class(self):
    #     return self._table_class


    # @table_class.setter
    # def table_class(self, value: type):
    #     self.__map = {getattr(item[1], 'name'):item[0] for item in vars(value) if hasattr(item[1], 'name')}

    #     self._table_class = value