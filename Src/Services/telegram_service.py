from DB.DBHelper import DBInterface
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager
from Src.Models import User, Message, Feature, Subscribe
from Src.event_handler import event_handler
from aiogram import types
from functools import singledispatchmethod
from datetime import datetime, timedelta
from DB.Tables import SubscribeInfo



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


    def get_features(self) -> dict[int:Message]:
        '''
        Получить словарь сообщений для рассылки раз в день.

        В словаре ключ это chat_id, а значение Message который надо отправить.
        '''
        users = self.__db.get(User)
        # Если будет высокая нагрузка на БД, то features можно выгрузить заранее
        features = self.__db.get(Feature)
        # Загрузить данные из таблицы подписок 
        messages = {}
        

        for user in users:
            subscribes = self.__db._get_ones(SubscribeInfo, user.id)
            if len(subscribes)==0:
                continue

            subscribe= sorted(subscribes, key=lambda x: x.subscribe_id)[-1]

            if subscribe.subscribe_start is None or subscribe.subscribe_end is None or \
            subscribe.subscribe_start > datetime.now() or subscribe.subscribe_end < datetime.now():
                messages[user.id] = self.__dilogue.get_start()

            delta = datetime.now() - subscribe.subscribe_start + timedelta(days=subscribe.count_subskribe_day)



        #     messages[user.id] = features[delta.days].message


        return messages


    def __handle(self, user: User, message: types.Message, next_message: Message) -> Message:
        '''
        Базовый обработчик сообщений
        '''
        print(user.current_message)
        print(next_message)
        last_message = user.current_message
        user.current_message = next_message
        output = user.current_message

        if next_message.event_name:

            # # Если при работе event будет ошибка, отправляем старое сообщение заного
            # try:
            output = self.__events.get_event(next_message.event_name).activate(user, message)
            # except Exception as e:
            #     # Временно сделана отловка всех ошибок, при логировании поменять
            #     print(e)
            #     return last_message

        
        self.__db.update(user)
        return output


    def handle_command(self, user: User, message: types.Message) -> Message:
        '''
        Обработчик команд
        '''
        next_message = self.__commands.get(message.text)
        return self.__handle(user, message, next_message)


    def handle_message(self, user: User, message: types.Message) -> Message:
        '''
        Обработчик сообщений
        '''
        next_message = self.__dilogue.get_next(user.current_message)
        return self.__handle(user, message, next_message)

    
    def handle_callback(self, user: User, callback: types.CallbackQuery) -> Message:
        '''
        Обработчик кнопок
        '''
        next_message = self.__dilogue.get(int(callback.data))
        return self.__handle(user, callback.message, next_message)


    def create_answer(self, message: Message) -> dict:
        '''
        Создать аргументы для ответа в телеграм
        '''
        answer_kwargs = {'text': message.text}

        if message.keyboard: 
            answer_kwargs['reply_markup'] = message.keyboard.build_markup()

        return answer_kwargs


    def create_user(self, user_id: int, username: str = '') -> User:
        '''
        Создать нового пользователя
        '''
        user = User(True, False, username, self.__dilogue.get_start(), user_id)
        self.__db.add(user)
        return user


    def get_user(self, user_id: int) -> User:
        '''
        Получить пользователя по id
        '''
        if not len(self.__db.get_ones(User, user_id)) > 0:
            return self.create_user(user_id)
        
        return self.__db.get_one(User, user_id)
