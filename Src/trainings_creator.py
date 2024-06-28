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


    def __init__(self, programs: list[TrainingProgramm], \
                 blocks: list[TrainingBlock], exesises: list[TrainingExercise]) -> None:
        self.__exercise_prototype = exersise_prototype(exesises)
        self.__block_prototype = block_prototype(blocks)
        self.__program_prototype = training_prototype(programs)


    def get_training(self, person: TrainingPersonData, trainings_per_day: int = 8) \
                    -> Training:
        program = self.get_program(person)

        blocks = self.get_blocks(program, trainings_per_day)

        return self.get_exercise(blocks)


    def get_program(self, person: TrainingPersonData) -> TrainingProgramm:
        fitting_programs = self.__program_prototype.filter_person_training_model(person)

        return fitting_programs.sample()


    def get_blocks(self, program: TrainingProgramm, trainings_pe_day: int = 8) -> Training:
        person_training_blocks = Training()

        for cur_day, blocks in program.trainings.items():
            for cur_block in blocks:
                block = self.__block_prototype.filter_block_on_day(
                    cur_block.muscle, trainings_pe_day // len(blocks))

                person_training_blocks[int(cur_day)-1].append(block.sample())

        return person_training_blocks


    def get_exercise(self, blocks: Training) -> Training:
        person_training_execises = Training()

        for cur_day in blocks.keys():
            for cur_block in blocks[cur_day]:
                for cur_criteria in cur_block.exersices_criteria:
                    exercise = self.__exercise_prototype.filter_exercises_criteria(
                        cur_criteria).sample()

                    person_training_execises[cur_day].append(exercise)

        return person_training_execises
