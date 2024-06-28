from Src.Models import *
from Src.Enums.muscle_type import muscle_type
from Src.Enums.pattern_type import pattern_type
from Src.Enums.location_type import location_type
from Src.Prototypes.prototype import prototype
from random import sample

class exersise_prototype(prototype):
    '''прототип для фильтрации упражнений по критериям из Block_model'''
    __data:list[Exercise_model]=[]
    __is_error:bool=False



    def __init__(self,data:list[Exercise_model]):
        if len(data)==0:
            self.__is_error=True
        self.__data=data

    
    def filter_exercises_criteria(self,criteria:list[muscle_type,location_type,pattern_type]):
        '''фильтрация'''
        if self.__is_error:
            return self.__data
    
        result=[]


        for cur_exersise in self.__data:
            if cur_exersise.muscle.name==criteria[0].name and \
            cur_exersise.locations.name==criteria[1].name and \
            cur_exersise.pattern.name==criteria[2].name:
                result.append(cur_exersise)
        

        return exersise_prototype(result)
    
    def sample(self, amount: int = 1):
        '''взять n случайных элементов из прототипа'''
        return sample(self.__data,amount)
    
    @property
    def data(self):
        return self.__data
