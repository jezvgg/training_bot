from  Src.Enums.abstract_type import abstract_type


class workout_type(abstract_type):

    def __init__(self, name: str) -> None:
        super().__init__(name)