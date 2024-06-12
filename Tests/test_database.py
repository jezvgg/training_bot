from DB.DBHelper import DBHelper
from Src.Models import *
import unittest


class test_database(unittest.TestCase):
    '''
    Тестирование работы и связи с базой данных
    '''

    dbh = DBHelper('test', '1111', '127.0.0.1', '5432', 'test')

    # TODO: дописать тестирование
    def test_starting_database(self):
        '''
        Проверка на работоспособность подключения
        '''

        # Спецальная роль в PostgreSQL
        dbh = DBHelper('test', '1111', '127.0.0.1', '5432', 'test')

        assert dbh is not None


    def test_get(self):
        result = self.dbh.get(User)

        assert result is not None


    def test_get_one(self):
        user = self.dbh.get(User)[0].model()

        result = self.dbh.get_one(user, user.id)

        assert result is not None


    def test_get_ones(self):
        user = self.dbh.get(User)[0].model()

        result = self.dbh.get_ones(user, user.id)

        assert result is not None
        assert len(result) > 0


    def test_get_models(self):
        result = self.dbh.get_models(User)

        assert result is not None
        assert len(result) > 0
        assert type(result[0]) == User


    def test_get_one_model(self):
        user = self.dbh.get_models(User)[0]

        result = self.dbh.get_one_model(user, user.id)

        assert result is not None
        assert type(result) == User


    def test_get_ones_models(self):
        user = self.dbh.get_models(User)[0]

        result = self.dbh.get_ones_models(user, user.id)

        assert result is not None
        assert len(result) > 0
        assert type(result[0]) == User
        