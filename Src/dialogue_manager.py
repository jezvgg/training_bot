from Src.Models import Message


# TODO: Сделать из этого итератор
class dialogue_manager:
    '''
    Класс для работы и управлением сообщениями.
    '''
    __messages: dict[int, Message]


    def __init__(self, messages: list[Message]):
        '''
        Args:
            messages - список моделей Message
        '''
        self.__messages = {}
        for message in messages:
            self.__messages[message.id] = message


    def get_start(self):
        '''
        Получить стартовое сообщение (первое)
        '''
        key = list(self.__messages.keys())[0]
        return self.__messages[key]


    def get_next(self, message: Message):
        '''
        Получить следующее сообщние от текущего.
        '''
        if message.next_message_id not in self.__messages.keys():
            raise Exception('Невозможно получить следующее сообщение. Оно отсутствует.')

        return self.__messages[message.next_message_id]