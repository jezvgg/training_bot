#тогда проще будет сделать поля типа bool: home, gym и берём данные оттуда
from  Src.Enums.abstract_type import abstract_type

#класс для локации
class location_type(abstract_type):
    __name=''

    def __init__(self, name: str) -> None:
        super().__init__(name)

    