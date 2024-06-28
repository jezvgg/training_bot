from Src.Models import AbstractModel
from dataclasses import dataclass


@dataclass
class training_base(AbstractModel):
    __name: str = ""

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):

        value_striped = value.strip()

        self.__name = value_striped
