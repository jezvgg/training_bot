from DB.DBHelper import DBHelper
from Src.Models import *
from Src.settings import settings
import unittest


class test_database(unittest.TestCase):
    '''
    Тестирование работы и связи с базой данных
    '''
    sets = settings('test', '1111', '127.0.0.1', '5432', 'test', 'token')
    dbh = DBHelper(sets)

    def test_starting_database(self):
        '''
        Проверка на работоспособность подключения
        '''

        # Спецальная роль в PostgreSQL
        dbh = DBHelper(self.sets)

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
        

    def test_add(self):
        user = User(True, False, '', Message.error_message(), False, 1)
        
        result = self.dbh.add(user)

        assert type(result) is bool

    
    def test_update(self):
        user = self.dbh.get_models(User)[0]

        user.username = user.username + '_'
        result = self.dbh.update(user)

        assert result is True