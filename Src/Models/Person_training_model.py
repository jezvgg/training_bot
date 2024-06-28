from Src.Models import training_base
from Src.Enums.workout_type import workout_type
from dataclasses import dataclass, field


@dataclass
class Person_training_model(training_base):
    '''
    Модель пользовательских требований к тренировке
    '''
    __is_male: bool = False
    __trains_per_week: int = 0
    __workout: list[workout_type] = field(default_factory=list[workout_type])

    def add_workout(self, value: workout_type) -> bool:
        '''
        Добавить тип тренировки
        '''
        self.__workout.append(value)
        return True

    def clear_workout(self) -> bool:
        '''
        Очистить типы тренировок
        '''
        self.__workout.clear()
        return True

    @property
    def workout(self) -> list[workout_type]:
        '''
        Типы тренировок
        '''
        return self.__workout

    @property
    def is_male(self) -> bool:
        '''Пол'''
        return self.__is_male

    @property
    def trains_per_week(self) -> int:
        '''
        Количество тренировок в неделю
        '''
        return self.__trains_per_week

    @is_male.setter
    def is_male(self, value: bool) -> None:
        self.__is_male = value

    @trains_per_week.setter
    def trains_per_week(self, value: int) -> None:

        if value < 0 or value > 6:
            raise Exception("value must be between 1 and 5")
            
        self.__trains_per_week = value
