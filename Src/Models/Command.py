from Src.Models import AbstractModel, Message


class Command(AbstractModel):
    '''
    Модель команд бота (например /start)
    '''
    __name: str
    __message: Message
    __description: str


    def __init__(self, description: str, message: Message, name: str) -> None:
        '''
        Модель команд бота (например /start)

        Args:
            description - описание команды (на будущее)
            message - сообщение, к которому ведёт команда
            name - сама команда (без черты)
        '''
        self.__name: str = name
        self.__message: Message = message
        self.__description: str = description


    @property
    def name(self) -> str:
        '''сама команда (без черты)'''
        return '/' + self.__name


    @property
    def message(self) -> Message:
        '''message - сообщение, к которому ведёт команда'''
        return self.__message


    @property
    def description(self) -> str:
        '''описание команды (на будущее)'''
        return self.__description