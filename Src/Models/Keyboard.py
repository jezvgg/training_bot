from Src.Models.AbstractModel import AbstractModel
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Keyboard(AbstractModel):
    '''
    Модель клавиатуры бота
    '''
    __id: int
    __data: list[dict[str,int]]


    def __init__(self, id:int, data: list[dict[str,int]]) -> None:
        '''
        Модель клавиатуры бота

        Args:
            id - уникальный номер клавиатуры
            data - список словарей, где каждый словарь строка, а элементы в нём - текст кнопки и id сообщения к которому она ведёт
        '''
        self.__data: list[dict[str,int]] = data
        self.__id = id


    def build_markup(self):
        inline_buttons = [
            [InlineKeyboardButton(text=text, callback_data=f'{message_id}') 
            for text, message_id in row.items()] 
            for row in self.__data]

        return InlineKeyboardMarkup(inline_keyboard=inline_buttons)


    @property
    def id(self) -> int:
        return self.__id


    @property
    def data(self) -> list[dict[str,int]]:
        return self.__data