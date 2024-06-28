
from Src.Models.training_base import training_base
from Src.Enums.muscle_type import muscle_type
from Src.Enums.location_type import location_type
from Src.Enums.pattern_type import pattern_type
from dataclasses import dataclass, field


@dataclass
class Block_model(training_base):
    """
    Модель блока в тренировке
    """
    __muscle: muscle_type = None
    __exersices_criteria: list = field(default_factory=list[list[muscle_type, location_type, pattern_type]])

    def add_block(self) -> None:
        '''
        добавить упражние в блок
        '''
        if self.count > 8:
            raise Exception("MAXIMUM VALUE OF TRAININGS PER WEEK IS 8")

        self.__exersices_criteria.append([])

    def add_critery(self, muscle: muscle_type, location: location_type, pattern: pattern_type, index: int = -1):
        '''
        добавить критерии в упражнение
        '''
        self.__exersices_criteria[index] = [muscle, location, pattern]

    @property
    def muscle(self) -> muscle_type:
        '''мышца'''
        return self.__muscle

    @property
    def exersices_criteria(self) -> list:
        '''критерии'''
        return self.__exersices_criteria

    @property
    def count(self) -> int:
        '''количество упражнений в блоке'''
        return len(self.__exersices_criteria)

    @muscle.setter
    def muscle(self, value: muscle_type) -> None:
        self.__muscle = value
