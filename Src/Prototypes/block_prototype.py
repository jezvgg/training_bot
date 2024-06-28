from Src.Models import *
from Src.Enums.muscle_type import muscle_type
from Src.Enums.pattern_type import pattern_type
from Src.Enums.location_type import location_type
from Src.Prototypes.prototype import prototype
from random import sample

class block_prototype(prototype):
    '''прототип для фильтрации блоков по нужной мышце и количеству упражнений в блоке'''
    __data:list[Block_model]=[]
    __is_error:bool=False



    def __init__(self,data:list[Block_model]):
        if len(data)==0:
            self.__is_error=True
        self.__data=data

    
    def filter_block_on_day(self,muscle:muscle_type,amount_of_exercises:int):
        '''фильтрация'''
        if self.__is_error:
            return self.__data
    
        result=[]


        for cur_block in self.__data:
            if cur_block.muscle.name==muscle.name and \
            abs(cur_block.count-amount_of_exercises)<=2:
                result.append(cur_block)
        

        return block_prototype(result)
    
    #sample and samples
    def sample(self, amount: int = 1):
        '''взять n случайных элементов из прототипа'''
        return sample(self.__data,amount)
    
    @property
    def data(self):
        return self.__data
