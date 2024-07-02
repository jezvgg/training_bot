from Src.Models import training_base
from Src.Enums.workout_type import workout_type
from dataclasses import dataclass, field


@dataclass
class TrainingPersonData(training_base):
    '''
    Модель пользовательских требований к тренировке
    '''
    gender: bool = False
    __traing_per_week: int = field(init=False, repr=False)
    trains_per_week: int = 0
    workout: list[workout_type] = field(default_factory=list[workout_type])


    @property
    def trains_per_week(self):
        '''количество тренировок в неделю'''
        return self.__trains_per_week


    @trains_per_week.setter
    def trains_per_week(self, value: int) -> None:

        if value < 0 or value > 6:
            raise Exception("value must be between 1 and 5")
            
        self.__trains_per_week = value
