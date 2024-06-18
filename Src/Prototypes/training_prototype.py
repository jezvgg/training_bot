from Src.Models.Models_for_training.program_model import Weekly_program_model
from Src.Models.Models_for_training.person_training_model import person_training_model

class Training_prototype:
    __data:list[Weekly_program_model]=[]
    __is_error:bool=False



    def __init__(self,data:list[Weekly_program_model]):
        if len(data)==0:
            self.__is_error=True
        self.__data=data

    
    def filter_person_training_model(self,user:person_training_model):
        if self.__is_error:
            return self.__data
    
        result=[]


        for cur_program_model in self.__data:
            if cur_program_model.is_male==user.is_male and \
            cur_program_model.workout==user.workout and \
            cur_program_model.trainings==user.trains_per_week:
                result.append(cur_program_model)
        

        return Training_prototype(result)




