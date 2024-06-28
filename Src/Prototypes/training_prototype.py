from Src.Models.Models_for_training.program_model import Weekly_program_model
from Src.Models.Models_for_training.person_training_model import Person_training_model
from Src.Enums.workout_type import workout_type
from Src.Prototypes.prototype import prototype
from random import sample

class training_prototype(prototype):
    '''прототип для фильтрациии програм на неделю по требованиям пользователя'''
    __data:list[Weekly_program_model]=[]
    __is_error:bool=False



    def __init__(self,data:list[Weekly_program_model]):
        if len(data)==0:
            self.__is_error=True
        self.__data=data

    @staticmethod
    def _equal_workouts(work1:list[workout_type],work2:list[workout_type])->bool:
        '''сравнение типов тренировок'''
        if len(work1)!=len(work2):
            return False
        ret=True
        for i in range(len(work1)):
            ret*=(work1[i].name==work2[i].name)
        return ret
    
    def filter_person_training_model(self,user:Person_training_model):
        '''фильтрация'''
        if self.__is_error:
            return self.__data
    
        result=[]


        for cur_program_model in self.__data:
            
            if cur_program_model.is_male==user.is_male and \
            training_prototype._equal_workouts(cur_program_model.workout,user.workout) and \
            cur_program_model.workouts_per_week==user.trains_per_week:
                result.append(cur_program_model)
        

        return training_prototype(result)
    
    def sample(self, amount: int = 1):
        '''взять n случайных элементов из прототипа'''
        return sample(self.__data,amount)
    
    @property
    def data(self):
        return self.__data




