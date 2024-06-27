from DB.DBHelper import DBHelper
from DB.DBTest import DBTest
from Src.Models import *
from DB.Tables import *
from Src.settings import settings
from pathlib import Path
import unittest
from datetime import datetime


class test_database(unittest.TestCase):
    '''
    Тестирование работы и связи с базой данных
    '''
    sets = settings('test', '1111', Path('test_db.db').resolve(), '5432', 'test', 'sqlite:///{host}', '')
    dbh = DBHelper(sets)

    def test_starting_database(self):
        '''
        Проверка на работоспособность подключения
        '''

        # Спецальная роль в PostgreSQL
        dbh = DBHelper(self.sets)

        assert dbh is not None


    def test_get(self):
        result = self.dbh._get(UserTable)

        assert result is not None


    def test_get_one(self):
        print(self.dbh._get(UserTable).all())
        user = self.dbh._get(UserTable).all()[0].model()

        result = self.dbh._get_one(UserTable, user.id)

        assert result is not None


    def test_get_ones(self):
        user = self.dbh._get(UserTable)[0].model()

        result = self.dbh._get_ones(UserTable, user.id)

        assert result is not None
        assert len(result) > 0


    def test_get_models(self):
        result = self.dbh.get(User)

        assert result is not None
        assert len(result) > 0
        assert type(result[0]) == User


    def test_get_one_model(self):
        user = self.dbh.get(User)[0]

        result = self.dbh.get_one(user, user.id)

        assert result is not None
        assert type(result) == User


    def test_get_ones_models(self):
        user = self.dbh.get(User)[0]

        result = self.dbh.get_ones(user, user.id)

        assert result is not None
        assert len(result) > 0
        assert type(result[0]) == User
        

    def test_add(self):
        user = User(True, False, '', Message.error_message(), datetime.now(), datetime.now(), 1)
        
        result = self.dbh.add(user)

        assert type(result) is bool

    
    def test_update(self):
        user = self.dbh.get(User)[0]

        user.username = user.username + '_'
        result = self.dbh.update(user)

        assert result is True


    def test_db_test_init(self):
        db = DBTest(User(True, False, '', Message.error_message(), datetime.now(), datetime.now(), 1))

        assert db is not None

    def test_db_test_get(self):
        db = DBTest(User(True, False, '', Message.error_message(), datetime.now(), datetime.now(), 1))

        users = db.get(User)

        assert users is not None
        assert len(users) > 0

    def test_db_test_get_one(self):
        db = DBTest(User(True, False, '', Message.error_message(), datetime.now(), datetime.now(), 1))

        user = db.get_one(User, 1)

        assert user is not None
        assert user.id == 1

    def test_db_test_get_ones(self):
        db = DBTest(User(True, False, '', Message.error_message(), datetime.now(), datetime.now(), 1))

        users = db.get_ones(User, 1)

        assert users is not None
        assert len(users) > 0

    def test_db_test_add(self):
        db = DBTest(User(True, False, '', Message.error_message(), datetime.now(), datetime.now(), 1))

        users1 = db.get(User)[:]
        result = db.add(User(True, False, '', Message.error_message(), datetime.now(), datetime.now(), 1))
        users2 = db.get(User)[:]

        assert result is True
        assert len(users1) < len(users2)
