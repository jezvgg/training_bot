import unittest
from Src.Models import *
from DB.Tables import *
from DB.table_factory import table_factory


class test_models(unittest.TestCase):
    '''
    Проверка создания моделей таблиц, их функций (если таковые есть) и фабричных методов.
    '''

    def test_base_table(self):

        bt = BaseTable.build(AbstractModel)

        assert bt is not None

        assert bt.__repr__() != ''
        
    
    def test_user_table(self):
        ut = UserTable(0, True, 0, True, True)

        assert ut is not None

        message = Message(0, 'test text', 3)
        user = User(True, True, 'test username', message, True, 0)
        
        ut2 = UserTable.build(user)

        assert ut2 is not None

        user2 = ut.model()

        assert user2 is not None


    def test_message_table(self):
        mt = MessagesTable(0, 'test text')

        assert mt is not None


    def test_dialoue_table(self):
        dt = DialogueTable(0, 0, 0)

        assert dt is not None

        message = Message(0, 'test text', 3)

        dt2 = DialogueTable.build(message)

        assert dt2 is not None

        message = dt.model()

        assert message is not None


    def test_keyboards_table(self):
        kt = KeyboardsTable(0, [[0, 1, 2], [3, 4, 5]])

        assert kt is not None

        keyboard = Keyboard(0, [[0, 1, 2], [3, 4, 5]])

        kt2 = KeyboardsTable.build(keyboard)

        assert kt2 is not None

        keyboard = kt.model()

        assert keyboard is not None


    def test_commands_table(self):
        cmdt = CommandsTable('start', 0)

        assert cmdt is not None

        message = Message(1, 'Первое тестовое сообщение', 2)
        command = Command('', message, 'start')

        cmdt2 = CommandsTable.build(command)

        assert cmdt2 is not None

        command = cmdt.model()

        assert command is not None


    def test_table_factory(self):
        message = Message(0, 'test text', 3)
        user = User(True, True, 'test username', message, True, 0)

        mtc = table_factory.get(message)
        mto = table_factory.create(message)
        utc = table_factory.get(user)
        uto = table_factory.create(user)

        assert mtc is DialogueTable
        assert type(mto) is DialogueTable
        assert utc is UserTable
        assert type(uto) is UserTable
        