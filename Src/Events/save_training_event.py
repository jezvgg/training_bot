from Src.Events.base_save_event import base_save_event
from DB.DBInterface import DBInterface
from DB.Tables import TrainingInfoTable, UserInfoTable, BlockTable, ExerciseTable, ProgramTable
from Src.Models import Message, Keyboard, User
from Src.Enums import workout_type
from Src.trainings_creator import trainings_getter
from aiogram import types


class save_training_event(base_save_event):
    '''
    опрос пользователя по данным для формирования тренировки.
    '''
    __creator: trainings_getter


    def __init__(self, db: DBInterface):
        super().__init__(db)

        self.table_class = TrainingInfoTable
        self.types = {
            TrainingInfoTable.trainings_per_week.name: int,
            TrainingInfoTable.workout.name: lambda x: {'похудение': ['weight loss'], 'функциональность': [
                'functional'], 'комплекс и накачка': ['complex', 'pumping']}[x]
        }

        blocks = self._db.get(BlockTable)
        exercises = self._db.get(ExerciseTable)
        programs = self._db.get(ProgramTable)

        self.__creator = trainings_getter(programs, blocks, exercises)


    def _start(self, user: User, message: types.Message) -> Message:
        '''
        Метод, который вызывается в начале опроса
        '''
        if self._start_message is None:
            self._start_message = user.current_message.id

        table = self._table_class(user.id, self._db._get_one(UserInfoTable, user.id).gender)
        self._db._add(table)

        return user.current_message


    def _finish(self, user: User, message: types.Message) -> Message:
        '''метод в конце опроса. отправляет расписание'''

        person = self._db._get_one(TrainingInfoTable, user.id)
        training = self.__creator.get_training(person.model(), 6)
        person.training = training.json()
        self._db._update()

        finish_message = Message(0, str(training), 0)
        print(finish_message)
        return finish_message


    def activate(self, user: User, message: types.Message) -> Message:
        '''активация ивента'''
        if len(self._db._get_ones(TrainingInfoTable, user.id)) == 0 or \
            sorted(self._db._get_ones(TrainingInfoTable, user.id), key=lambda x: x.training_id)[-1].training is not None :
            return self._start(user, message)

        return self._next(user, message)
