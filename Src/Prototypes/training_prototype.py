from Src.Models import Weekly_program_model
from Src.Models import Person_training_model
from Src.Enums.workout_type import workout_type
from Src.Prototypes import prototype
from random import sample


class training_prototype(prototype):
    '''Прототип для фильтрациии програм на неделю по требованиям пользователя'''
    _data: list[Weekly_program_model]


    @staticmethod
    def _equal_workouts(work1: list[workout_type], work2: list[workout_type]) -> bool:
        '''сравнение типов тренировок'''
        # Нужно было создать __hash__, и сравнивать множества напрямую
        if len(work1) != len(work2):
            return False
        ret = True
        for i in range(len(work1)):
            ret *= (work1[i].name == work2[i].name)
        return ret


    def filter_person_training_model(self, user: Person_training_model):
        '''фильтрация'''
        result = []

        for cur_program_model in self._data:
            if cur_program_model.is_male == user.is_male and \
                    training_prototype._equal_workouts(cur_program_model.workout, user.workout) and \
                    cur_program_model.workouts_per_week == user.trains_per_week:
                result.append(cur_program_model)

        return training_prototype(result)

