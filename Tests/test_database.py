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

        # Спецальная роль в PostgreSQL
        dbh = DBHelper('test', '1111', '127.0.0.1', '5432', 'training_bot')

        assert dbh is not None

