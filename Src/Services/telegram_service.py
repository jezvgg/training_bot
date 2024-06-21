from DB.DBHelper import DBInterface
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager
from Src.Models import User, Message
from Src.event_handler import event_handler
from aiogram import types
from functools import singledispatchmethod


class telegram_service:
    '''
    Сервис реализующий логику работы телеграм эндпоинт
    '''
    __db: DBInterface
    __dilogue: dialogue_manager
    __commands: command_manager
    __events: event_handler


    def __init__(self, dilogue: dialogue_manager, commands: command_manager, helper: DBInterface):
        self.__db = helper
        self.__dilogue = dilogue
        self.__commands = commands
        self.__events = event_handler(self.__db)


    def handle_command(self, user: User, message: types.Message) -> Message:
        next_message = self.__commands.get(message.text)
        user.current_message = next_message
        self.__db.update(user)

        if next_message.event_name:
            return self.__events.get_event(next_message.event_name).activate(user, message)
        return next_message


    def handle_message(self, user: User, message: types.Message) -> Message:
        next_message = self.__dilogue.get_next(user.current_message)
        user.current_message = next_message
        self.__db.update(user)

        if next_message.event_name:
            return self.__events.get_event(next_message.event_name).activate(user, message)
        return next_message

    
    def handle_callback(self, user: User, callback: types.CallbackQuery) -> Message:
        next_message = self.__dilogue.get(int(callback.data))
        user.current_message = next_message
        self.__db.update(user)

        if next_message.event_name:
            return self.__events.get_event(next_message.event_name).activate(user, callback.message)
        return next_message

    def create_answer(self, message: Message) -> dict:
        '''
        Создать аргументы для ответа в телеграм
        '''
        answer_kwargs = {'text':message.text}

        if message.keyboard: 
            answer_kwargs['reply_markup'] = message.keyboard.build_markup()

        return answer_kwargs


    def create_user(self, user_id: int, username: str = '') -> User:
        '''
        Создать нового пользователя
        '''
        user = User(True, False, username, self.__dilogue.get_start(), False, user_id)
        self.__db.add(user)
        return user


    def get_user(self, user_id: int) -> User:
        '''
        Получить пользователя по id
        '''
        if not self.__db.get_ones(User, user_id):
            return self.create_user(user_id)
        
        return self.__db.get_one(User, user_id)
