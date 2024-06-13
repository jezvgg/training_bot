from Src.Models import AbstractModel, Message


class Command(AbstractModel):
    '''
    Модель команд бота (например /start)
    '''
    __name: str
    __message: Message
    __description: str


    def __init__(self, description: str, message: Message, name: str) -> None:
        self.__name: str = name
        self.__message: Message = message
        self.__description: str = description


    @property
    def name(self) -> str:
        return '/' + self.__name


    @property
    def message(self) -> Message:
        return self.__message


    @property
    def description(self) -> str:
        return self.__description