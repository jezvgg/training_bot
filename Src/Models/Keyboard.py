from Src.Models.AbstractModel import AbstractModel

from dataclasses import dataclass,field


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dataclass
class Keyboard(AbstractModel):
    '''
    Модель клавиатуры бота
    '''
    __id: int
    __data: list[list[int|str]]=field(default_factory=list[list[int|str]])



    def build_markup(self):
        return InlineKeyboardMarkup(inline_keyboard=self.__buttons)


    @property
    def id(self) -> int:
        return self.__id


    @property
    def data(self) -> list[dict[str,int]]:
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