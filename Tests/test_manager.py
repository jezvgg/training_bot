import unittest
from Src.Models import *
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager


class test_dialogue(unittest.TestCase):
    '''
    Тестирование способности бота введения диалога (dialogue_manager)
    '''
    def test_dialogue_messages(self):
        '''
        Смотрим что у нас правильно получается первое сообщение и правильно работает переход между сообщениями.
        '''
        msg1 = Message(1, 'Первое сообщение', 2)
        msg2 = Message(2, 'Второе сообщение', 4)
        msg3 = Message(3, 'Последнее сообщение', 4)
        msg4 = Message(4, 'Рекурсионное сообщение', 3)

        messages = [msg1,
                    msg2,
                    msg3,
                    msg4]

        manager = dialogue_manager(messages)

        first_msg = manager.get_start()
        assert first_msg == msg1
        print(first_msg.text)
        second_msg = manager.get_next(first_msg)
        assert second_msg == msg2
        print(second_msg.text)
        thrid_msg = manager.get_next(second_msg)
        assert thrid_msg == msg4
        print(thrid_msg.text)
        fourth_msg = manager.get_next(thrid_msg)
        assert fourth_msg == msg3
        print(fourth_msg.text)
        to_recursion_msg = manager.get_next(fourth_msg)
        assert to_recursion_msg == msg4
        print(to_recursion_msg.text)


    def test_commands_manager(self):
        '''
        Смотрим что у нас правильно вызываются сообщения от команд
        '''

        msg1 = Message(1, 'Первое сообщение', 2)
        msg2 = Message(2, 'Второе сообщение', 4)
        msg3 = Message(3, 'Последнее сообщение', 4)
        msg4 = Message(4, 'Рекурсионное сообщение', 3)

        commands = [Command('', msg1, 'start'),
                    Command('', msg2, 'next'),
                    Command('', msg3, 'training'),
                    Command('', msg4, 'get_last')]

        manager = command_manager(commands)

        assert manager.get('/start') == msg1
        assert manager.get('/next') == msg2
        assert manager.get('/get_last') == msg4
        
        