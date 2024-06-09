
from models_for_training.field_types.abstract_type import abstract_type


class pattern_type(abstract_type):
    __name=''
    def __init__(self, name: str) -> None:
        super().__init__(name)