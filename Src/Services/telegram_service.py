from DB.DBHelper import DBHelper
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager
from Src.Models import User, Message
from Src.event_handler import event_handler


class telegram_service:
    '''
    Сервис реализующий логику работы телеграм эндпоинт
    '''
    __db: DBHelper
    __dilogue: dialogue_manager
    __commands: command_manager


    @staticmethod
    def create_answer(user: User, message: Message = None) -> dict:
        '''
        Создать аргументы для ответа в телеграм
        '''
        if not message: message = user.current_message
        
        answer_kwargs = {'text':message.text}

        if message.event_name:
            event = event_handler.get_event(message.event_name).activate(user, message)
            answer_kwargs['text'] = answer_kwargs['text'].format(event=event)

        if message.keyboard: 
            answer_kwargs['reply_markup'] = message.keyboard.build_markup()

        return answer_kwargs


    def __init__(self, dilogue: dialogue_manager, commands: command_manager, helper: DBHelper):
        self.__db = helper
        self.__dilogue = dilogue
        self.__commands = commands


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
        if len(self.__db.get_ones(User, user_id)) == 0:
            return self.create_user(user_id)
        
        return self.__db.get_one_model(User, user_id)
