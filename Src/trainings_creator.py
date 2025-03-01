from Src.Models import *
from Src.Prototypes import *
from Src.Enums import workout_type


class trainings_getter:
    '''
    Класс для создания тренеровок
    '''
    __block_prototype: block_prototype
    __program_prototype: training_prototype
    __exercise_prototype: exersise_prototype


    def __init__(self, programs: list[TrainingProgramm], \
                 blocks: list[TrainingBlock], exesises: list[TrainingExercise]) -> None:
        '''
        args:
            programs - list[TrainingProgramm] список программ
            blocks - list[TrainingBlock] список блоков
            exesises - list[TrainingExercise] список упражнений

        '''
        self.__exercise_prototype = exersise_prototype(exesises)
        self.__block_prototype = block_prototype(blocks)
        self.__program_prototype = training_prototype(programs)


    def get_training(self, person: TrainingPersonData, trainings_per_day: int = 8) \
                    -> Training:
        '''
        получить расписание тренировок на неделю
        args:
            person - TrainingPersonData информация о пользователе
            
            trainings_per_day - тренировок в день
        '''
        program = self.get_program(person)

        blocks = self.get_blocks(program, trainings_per_day)

        return self.get_exercise(blocks)


    def get_program(self, person: TrainingPersonData) -> TrainingProgramm:
        '''
        получить программу TrainingProgramm
        args:
            person - TrainingPersonData информация о пользователе
        '''
        fitting_programs = self.__program_prototype.filter_person_training_model(person)

        return fitting_programs.sample()


    def get_blocks(self, program: TrainingProgramm, trainings_pe_day: int = 8) -> Training:
        '''
        получить словарь из блоков по программе триноровок
        args:
            program - TrainingsProgramm программа тренировок

            trainings_pe_day - количество тренировок в день
        '''

        person_training_blocks = Training()

        for cur_day, blocks in program.trainings.items():
            for cur_block in blocks:
                block = self.__block_prototype.filter_block_on_day(
                    cur_block.muscle, trainings_pe_day // len(blocks)).sample()

                person_training_blocks[int(cur_day)-1].append(block)

        return person_training_blocks


    def get_exercise(self, blocks: Training) -> Training:
        '''
        получить упражнения по блокам
        args:
            blocks - Training модель тренировки
        '''
        person_training_execises = Training()

        for cur_day in blocks.keys():
            for cur_block in blocks[cur_day]:
                for cur_criteria in cur_block.exersices_criteria:
                    exercises = self.__exercise_prototype.filter_exercises_criteria(
                        cur_criteria)

                    exercise = exercises.sample()
                    # Мало упражнений, чтоб делать уникальные тренировки
                    # while exercise in person_training_execises[cur_day]:
                    #     print(exercises.data)
                    #     exercises.data.remove(exercise)
                    #     exercise = exercises.sample()

                    person_training_execises[cur_day].append(exercise)

        return person_training_execises


if __name__ == '__main__':
    from DB.DBHelper import DBHelper
    from Src.settings import settings
    sets = settings.from_json()
    db = DBHelper(sets)
    creator = trainings_getter(db.get(TrainingProgramm), db.get(TrainingBlock), db.get(TrainingExercise))
    person = TrainingPersonData("", True, 3, [workout_type('complex'), workout_type('pumping')])

    training = creator.get_training(person, 6)

    print(training)