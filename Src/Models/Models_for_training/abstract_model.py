from abc import ABC
from dataclasses import dataclass

@dataclass
class abstract_reference(ABC):

    __name:str = ""

    def __str__(self) -> str:
        return self.name

    @property    
    def name(self)->str:
        return self.__name 
   
    
    @name.setter 
    def name(self, value: str):

        value_striped=value.strip()

        self.__name = value_striped

    

