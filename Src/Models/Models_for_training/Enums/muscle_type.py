
from Src.Models.Models_for_training.Enums.abstract_type import abstract_type

class muscle_type(abstract_type):
    __name=''
    
    def __init__(self, name: str) -> None:
        super().__init__(name)