from Src.Models.Models_for_training.program_model import Weekly_program_model
from Src.Models.Models_for_training.person_training_model import Person_training_model
from Src.Enums.workout_type import workout_type

class Training_prototype:
    __data:list[Weekly_program_model]=[]
    __is_error:bool=False



    def __init__(self,data:list[Weekly_program_model]):
        if len(data)==0:
            self.__is_error=True
        self.__data=data

    @staticmethod
    def _equal_workouts(work1:list[workout_type],work2:list[workout_type])->bool:
        if len(work1)!=len(work2):
            return False
        ret=True
        for i in range(len(work1)):
            ret*=(work1[i].name==work2[i].name)
        return ret
    
    def filter_person_training_model(self,user:Person_training_model):
        if self.__is_error:
            return self.__data
    
        result=[]


        for cur_program_model in self.__data:
            
            if cur_program_model.is_male==user.is_male and \
            Training_prototype._equal_workouts(cur_program_model.workout,user.workout) and \
            cur_program_model.workouts_per_week==user.trains_per_week:
                result.append(cur_program_model)
        

        return Training_prototype(result)
    
    @property
    def data(self):
        return self.__data




