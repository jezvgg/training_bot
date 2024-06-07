from DB.DBHelper import DBHelper
import unittest


class test_database(unittest.TestCase):
    '''
    Тестирование работы и связи с базой данных
    '''

    dbh: DBHelper

    # TODO: дописать тестирование
    def test_starting_database(self):
        '''
        Проверка на работоспособность подключения
        '''

        # Спецальная роль в PostgreSQL
        self.dbh = DBHelper('test', '1111', '127.0.0.1', '5432', 'test')

        assert self.dbh is not None

