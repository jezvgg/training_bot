from Src.Models import Message, AbstractModel
from dataclasses import dataclass

@dataclass
class Diet(AbstractModel):
    '''
    Модель меню
    '''
    __telegram_id: int #id Пользователя
    __product: str #Продукты на которые у пользователя аллергия или которые он не любит
    __diet_goal: str #Последнее сохраненное меню
    __count_trainigs: int #Колво тренировок в неделю


    
    @property
    def id(self) -> int:
        return self.__telegram_id


    @property
    def product(self) -> str:
        return self.__product


    @product.setter
    def product_alerg(self, value : str) -> None:
        self.__product = value


    @property
    def diet_goal(self) -> str:
        return self.__diet_goal


    @diet_goal.setter
    def diet_goal(self, value : str) -> None:
        self.__diet_goal = value

    @property
    def count_trainigs(self) -> int:
        return self.__count_trainigs


    @count_trainigs.setter
    def count_trainigs(self, value : int) -> None:
        self.__count_trainigs = value



