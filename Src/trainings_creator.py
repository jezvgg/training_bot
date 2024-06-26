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



    def get_training(self,trainings_per_day:int=8)->defaultdict[int:list[Exercise_model]]:
        program=self.get_program()

        blocks=self.get_blocks(program,trainings_per_day)

        return self.get_exercise(blocks)



    def get_program(self)->Weekly_program_model:
        fitting_programs=self.__program_prototype.filter_person_training_model(self.__person)

        return fitting_programs.sample()[0]

    
    def get_blocks(self,program:Weekly_program_model,trainings_pe_day:int=8)->defaultdict[int:list[Block_model]]:
        person_training_blocks=defaultdict(lambda:[])

        for cur_day in program.trainings:
            trainings_per_block=trainings_pe_day//len(program.trainings[cur_day])

            for cur_block in program.trainings[cur_day]:
                fitting_blocks=self.__block_prototype.filter_block_on_day(cur_block.muscle,trainings_per_block)

                block=fitting_blocks.sample()[0]

                added=person_training_blocks[cur_day]
                added.append(block)
                person_training_blocks[cur_day]=added
        
        return person_training_blocks




    def get_exercise(self,blocks:defaultdict[int:list[Block_model]])->defaultdict[int:list[Exercise_model]]:
        person_training_execises=defaultdict(lambda:[])
        for cur_day in blocks.keys():

            for cur_block in blocks[cur_day]:
                
                for cur_criteria in cur_block.exersices_criteria:
                    fitting_exercises=self.__exercise_prototype.filter_exercises_criteria(cur_criteria)

                    added=person_training_execises[cur_day]
                    added.append(fitting_exercises.sample()[0])
                    person_training_execises[cur_day]=added
            
        return person_training_execises