from abc import ABC


class abstract_reference(ABC):

    __name:str = ""

    
    def __init__(self, name: str = "untituled") -> None:
        self.name = name

    @property    
    def name(self)->str:
        return self.__name 
   
    
    @name.setter 
    def name(self, value: str):

        value_striped=value.strip()

        self.__name = value_striped

        

