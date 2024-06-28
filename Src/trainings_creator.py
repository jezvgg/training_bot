from Src.Models import *
from Src.Prototypes import *
from collections import defaultdict


class trainings_getter:
    '''
    Класс для создания тренеровок
    '''
    __block_prototype: block_prototype
    __program_prototype: training_prototype
    __exercise_prototype: exersise_prototype


    def __init__(self, programs: list[Weekly_program_model], \
                 blocks: list[Block_model], exesises: list[Exercise_model]) -> None:
        self.__exercise_prototype = exersise_prototype(exesises)
        self.__block_prototype = block_prototype(blocks)
        self.__program_prototype = training_prototype(programs)


    def get_training(self, person: Person_training_model, trainings_per_day: int = 8) \
                    -> defaultdict[int:list[Exercise_model]]:
        program = self.get_program(person)

        blocks = self.get_blocks(program, trainings_per_day)

        return self.get_exercise(blocks)


    def get_program(self, person: Person_training_model) -> Weekly_program_model:
        fitting_programs = self.__program_prototype.filter_person_training_model(person)

        return fitting_programs.sample()


    def get_blocks(self, program: Weekly_program_model, trainings_pe_day: int = 8) -> defaultdict[int:list[Block_model]]:
        person_training_blocks = defaultdict(lambda: [])

        for cur_day in program.trainings:
            trainings_per_block = trainings_pe_day // len(program.trainings[cur_day])

            for cur_block in program.trainings[cur_day]:
                fitting_blocks = self.__block_prototype.filter_block_on_day(
                    cur_block.muscle, trainings_per_block)

                block = fitting_blocks.sample()

                added = person_training_blocks[cur_day]
                added.append(block)
                person_training_blocks[cur_day] = added

        return person_training_blocks


    def get_exercise(self, blocks: defaultdict[int:list[Block_model]]) -> defaultdict[int:list[Exercise_model]]:
        person_training_execises = defaultdict(lambda: [])
        for cur_day in blocks.keys():

            for cur_block in blocks[cur_day]:

                for cur_criteria in cur_block.exersices_criteria:
                    fitting_exercises = self.__exercise_prototype.filter_exercises_criteria(
                        cur_criteria)

                    added = person_training_execises[cur_day]
                    added.append(fitting_exercises.sample())
                    person_training_execises[cur_day] = added

        return person_training_execises
