from Src.Models import Message


class Dialogue_manager:
    '''
    Класс для работы и управлением сообщениями.
    '''
    messages: dict[int, Message]


    def __init__(self, messages: dict[int, Message]):
        '''
        Args:
            messages - словарь, где ключ - id сообщения, а value - сообщение (Message)
        '''
        # TODO: добавить проверку messages на корректность
        self.messages = messages


    def get_start(self):
        '''
        Получить стартовое сообщение (первое)
        '''
        key = list(self.messages.keys())[0]
        return self.messages[key]


    def get_next(self, message: Message):
        '''
        Получить следующее сообщние от текущего.
        '''
        if message.next_message_id not in self.messages.keys():
            raise Exception('Невозможно получить следующее сообщение. Оно отсутствует.')

        return self.messages[message.next_message_id]