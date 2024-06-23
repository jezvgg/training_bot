from Src.Models import *
from random import sample
from Src.Prototypes.exercise_prototype import exersise_prototype




class trainings_getter:
    __program:Weekly_program_model
    __program_dict:dict[int:list[Exercise_model]]
    __blocks:list[Block_model]
    __exercises:list[Exercise_model]
    __prototype:exersise_prototype

    #какая идея- по листу blocks ищем подходящие блоки, и далее добираем до  8 упраажнений,
    #по листу - exercises ищем упражнения
    def __init__(self,program:Weekly_program_model=None,blocks:list[Block_model]=[],exesises:list[Exercise_model]=[]) -> None:
        self.__program=program
        self.__blocks=blocks
        self.__exercises=exesises
        self.__prototype=exersise_prototype(self.__exercises)
        self.__program_dict={}


    def create_training(self,exercises_per_day:int=8):
        for cur_day in self.__program.trainings:
            trainings_per_block=exercises_per_day//len(self.__program.trainings[cur_day])

            dayly_execises=self._take_exercises_from_block(trainings_per_block)

            #добавляем  в нужный день
            self.__program_dict[cur_day]=dayly_execises

    #фильтруем упражнения по блоку и возвращаем 3 рандомных
    def _take_exercises_from_block(self,exercises_amount:int):
        res=[]
        #написал хуйню
        #sample в прототип
        #res+=exercises
        #треню-в-модель
        for cur_block in self.__blocks:
            for cur_exer in cur_block.exersices_criteria:
                
                cur_prot=self.__prototype.filter_exercises_criteria(cur_exer)

                exercises=cur_prot.data
                exercises=sample(exercises,1)

                res.extend(exercises)
        return res
    
    @property
    def program(self):
        return self.__program_dict  
    