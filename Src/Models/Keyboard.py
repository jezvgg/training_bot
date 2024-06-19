from Src.Models.AbstractModel import AbstractModel

from dataclasses import dataclass,field


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

@dataclass
class Keyboard(AbstractModel):
    '''
    Модель клавиатуры бота
    '''
    __id: int

    __data: list[list[int|str]]=field(default_factory=list[list[int|str]])



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