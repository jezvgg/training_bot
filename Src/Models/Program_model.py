from Src.Models import training_base
from Src.Models import Block_model
from Src.Enums.workout_type import workout_type
from dataclasses import dataclass, field


@dataclass
class Weekly_program_model(training_base):
    '''
    Модель программы занятий на неделю
    '''
    __is_male: bool = True
    __workout: list[workout_type] = field(default_factory=list[workout_type])
    __trainings: dict = field(default_factory=dict[int:list[Block_model]])

    @property
    def is_male(self) -> bool:
        '''Пол'''
        return self.__is_male

    @property
    def workout(self) -> workout_type:
        '''
        Тип тренировок
        '''
        return self.__workout

    @property
    def workouts_per_week(self) -> int:
        '''
        Количество тренировок в неделю
        '''
        return len(list(self.__trainings.keys()))

    @property
    def trainings(self) -> dict[int:list[Block_model]]:
        '''
        Словарь типа {номер_дня:[блок1, блок2 ... блокn]}
        '''
        return self.__trainings

    @is_male.setter
    def is_male(self, value: bool) -> None:
        self.__is_male = value

    def add_workout_type(self, value: workout_type) -> None:
        '''
        Добавить тип тренировок
        '''
        self.__workout.append(value)

    def add_block(self, block: Block_model, day: int = 1) -> None:
        '''
        добавить блок в нужный день
        '''
        # TODO инвертировать логику
        if day < 1 or day > 5:
            raise Exception("Day must be from 1 to 5")

        if day in self.__trainings.keys():
            self.__trainings[day].append(block)
        else:
            self.__trainings[day] = [block]
