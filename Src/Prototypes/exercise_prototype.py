from Src.Models import *
from Src.Enums.muscle_type import muscle_type
from Src.Enums.pattern_type import pattern_type
from Src.Enums.location_type import location_type
from Src.Prototypes.prototype import prototype
from random import sample


class exersise_prototype(prototype):
    '''прототип для фильтрации упражнений по критериям из TrainingBlock'''
    _data: list[TrainingExercise]

    def filter_exercises_criteria(self, criteria: list[muscle_type, location_type, pattern_type]):
        '''Фильтрация'''
        # Комментарий недостаточно полный
        result = []

        for cur_exersise in self._data:
            if cur_exersise.muscle.name == criteria[0].name and \
                    cur_exersise.locations.name == criteria[1].name and \
                    cur_exersise.pattern.name == criteria[2].name:
                result.append(cur_exersise)

        return exersise_prototype(result)
