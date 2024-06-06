from Src.Models import Message, AbstractModel


class User(AbstractModel):
    __telegram_id: int
    __subcribed: bool
    __current_message: Message
    __username: str
    __is_accepted: bool
    __is_use: bool


    def __init__(self, is_use: bool, is_accepted: bool, username: str, current_message: Message, subcribed: bool, telegram_id: int) -> None:
        self.__telegram_id: int = telegram_id
        self.__subcribed: bool = subcribed
        self.__current_message: Message = current_message
        self.__username: str = username
        self.__is_accepted: bool = is_accepted
        self.__is_use: bool = is_use


    @property
    def telegram_id(self) -> int:
        return self.__telegram_id


    @property
    def subcribed(self) -> bool:
        return self.__subcribed


    @subcribed.setter
    def subcribed(self, value : bool) -> None:
        self.__subcribed = value


    @property
    def current_message(self) -> Message:
        return self.__current_message


    @current_message.setter
    def current_message(self, value : Message) -> None:
        self.__current_message = value


    @property
    def username(self) -> str:
        return self.__username


    @username.setter
    def username(self, value : str) -> None:
        self.__username = value


    @property
    def is_accepted(self) -> bool:
        return self.__is_accepted


    @is_accepted.setter
    def is_accepted(self, value : bool) -> None:
        self.__is_accepted = value


    @property
    def is_use(self) -> bool:
        return self.__is_use


    @is_use.setter
    def is_use(self, value : bool) -> None:
        self.__is_use = value