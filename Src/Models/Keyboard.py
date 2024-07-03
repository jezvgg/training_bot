from Src.Models.AbstractModel import AbstractModel
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Keyboard(AbstractModel):
    '''
    Модель клавиатуры бота
    '''
    __id: int
    __data: list[dict[str,int]]
    __buttons: list[list[InlineKeyboardButton]]


    def __init__(self, id:int, data: list[dict[str,int]]) -> None:
        '''
        Модель клавиатуры бота

        Args:
            id - уникальный номер клавиатуры
            data - список словарей, где каждый словарь строка, а элементы в нём - текст кнопки и id сообщения к которому она ведёт
        '''
        self.data = data
        self.__id = id


    def build_markup(self):
        return InlineKeyboardMarkup(inline_keyboard=self.__buttons)


    @property
    def id(self) -> int:
        '''уникальный номер клавиатуры'''
        return self.__id


    @property
    def data(self) -> list[dict[str,int]]:
        ''' список словарей, где каждый словарь строка, а элементы в нём - текст кнопки и id сообщения к которому она ведёт'''
        return self.__data


    @data.setter
    def data(self, value: list[dict[str,int]]) -> None:
        self.__buttons = [
            [InlineKeyboardButton(text=text, callback_data=f'{message_id}') 
            for text, message_id in row.items()] 
            for row in value]

        self.__data = value


    @property
    def _buttons(self) -> list[list[InlineKeyboardButton]]:
        return self.__buttons