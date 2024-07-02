from Src.Models import Message, AbstractModel
from dataclasses import dataclass




@dataclass
class Diet(AbstractModel):
    '''
    Модель меню
    '''
    __diet_id:int #id записи 
    __id: int #id Пользователя
    __product: str #Продукты на которые у пользователя аллергия или которые он не любит
    __diet_goal: str #Последнее сохраненное меню
    __count_trainigs: int #Колво тренировок в неделю
    __diet:str


    @property
    def diet_id(self) -> int:
        '''id записи '''
        return self.__diet_id


    @property
    def id(self) -> int:
        '''id Пользователя'''
        return self.__id


    @property
    def product(self) -> str:
        '''Продукты на которые у пользователя аллергия или которые он не любит'''
        return self.__product


    @product.setter
    def product_alerg(self, value : str) -> None:
        self.__product = value


    @property
    def diet_goal(self) -> str:
        '''Последнее сохраненное меню'''
        return self.__diet_goal


    @diet_goal.setter
    def diet_goal(self, value : str) -> None:
        self.__diet_goal = value

    @property
    def count_trainigs(self) -> int:
        '''Колво тренировок в неделю'''
        return self.__count_trainigs


    @count_trainigs.setter
    def count_trainigs(self, value : int) -> None:
        self.__count_trainigs = value


    @property
    def diet(self) -> str:
        '''описание диеты'''
        return self.__diet


    @diet.setter
    def diet(self, value : str) -> None:
        self.__diet = value



