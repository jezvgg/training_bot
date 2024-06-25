from Src.Models import *
from random import sample
from Src.Prototypes import *
from collections import defaultdict


#тогда делаем так - поул
class trainings_getter:

    __person:Person_training_model
    __person_program:Weekly_program_model


    __programs:list[Weekly_program_model]
    __blocks:list[Block_model]
    __exercises:list[Exercise_model]

    __block_prototype:block_prototype
    __program_prototype:training_prototype
    __exercise_prototype:exersise_prototype




    def __init__(self,person:Person_training_model=None,programs:list[Weekly_program_model]=[],blocks:list[Block_model]=[],exesises:list[Exercise_model]=[]) -> None:
        self.__person=person
        
        self.__programs=programs
        self.__blocks=blocks
        self.__exercises=exesises

        self.__exercise_prototype=exersise_prototype(self.__exercises)
        self.__block_prototype=block_prototype(self.__blocks)
        self.__program_prototype=training_prototype(self.__programs)



    #изолировать методы друг от друга, установить pretier
    def get_training(self,trainings_per_day:int=8):
        pass
        #self.get_program()


    def get_program(self):
        fitting_programs=self.__program_prototype.filter_person_training_model(self.__person)

        return fitting_programs.sample()[0]

    
    def get_blocks(self,trainings_pe_day:int=8):
        person_training_blocks=defaultdict(lambda:[])

        for cur_day in self.__person_program.trainings:
            trainings_per_block=trainings_pe_day//len(self.__person_program.trainings[cur_day])

            for cur_block in self.__person_program.trainings[cur_day]:
                fitting_blocks=self.__block_prototype.filter_block_on_day(cur_block.muscle_type,trainings_per_block)

                block=fitting_blocks.sample()[0]

                added=person_training_blocks[cur_day]
                added.append(block)
                person_training_blocks[cur_day]=added
        
        return person_training_blocks




    def get_exercise(self,blocks:defaultdict[int:Block_model]):
        person_training_execises=defaultdict(lambda:[])
        for cur_day in blocks.keys():

            for cur_block in blocks[cur_day]:
                
                for cur_criteria in cur_block.exersices_criteria:

                    fitting_exercises=self.__exercise_prototype.filter_exercises_criteria(cur_criteria)

                    added=person_training_execises[cur_day]
                    added.append(fitting_exercises.sample()[0])
                    person_training_execises[cur_day]=added
            
        return person_training_execises