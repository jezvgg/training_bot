from DB.DBHelper import DBHelper
import unittest
import os
import sys


class test_database(unittest.TestCase):
    '''
    Тестирование работы и связи с базой данных
    '''

    def test_starting_database(self):
        '''
        Проверка на работоспособность подключения
        '''
        # TODO: починить env vars
        print(sys.version_info, sys.path)
        print(os.environ, os.getenv('DB_USER'))

        dbh = DBHelper('postgres', 'your_password', '127.0.0.1', '5432', 'training_bot')

        assert dbh is not None

