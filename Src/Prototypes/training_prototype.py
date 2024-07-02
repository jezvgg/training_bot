from Src.Models import TrainingProgramm
from Src.Models import TrainingPersonData
from Src.Enums.workout_type import workout_type
from Src.Prototypes import prototype
from random import sample


class training_prototype(prototype):
    '''Прототип для фильтрациии програм на неделю по требованиям пользователя'''
    _data: list[TrainingProgramm]


    @staticmethod
    def _equal_workouts(work1: list[workout_type], work2: list[workout_type]) -> bool:
        '''сравнение типов тренировок'''
        # Нужно было создать __hash__, и сравнивать множества напрямую
        if len(work1) != len(work2):
            return False

        for i in range(len(work1)):
            if not work1[i].name == work2[i].name: return False
            
        return True


    def filter_person_training_model(self, user: TrainingPersonData):
        '''фильтрация'''
        result = []

        for cur_program_model in self._data:
            if cur_program_model.is_male == user.gender and \
                    training_prototype._equal_workouts(cur_program_model.workout, user.workout) and \
                    cur_program_model.workouts_per_week == user.trains_per_week:
                result.append(cur_program_model)

        return training_prototype(result)

