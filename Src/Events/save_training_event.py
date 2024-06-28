from Src.Events.base_save_event import base_save_event
from DB.DBInterface import DBInterface
from DB.Tables import TrainingInfoTable,UserInfoTable,BlockTable,ExerciseTable,ProgramTable
from Src.Models import Message, Keyboard, User
from Src.Enums import  workout_type
from Src.trainings_creator import trainings_getter
from aiogram import types


class save_training_event(base_save_event):
    '''
    опрос пользователя по данным для формирования тренировки.
    '''

    def __init__(self, db: DBInterface):
        super().__init__(db)
        
        self.table_class = TrainingInfoTable
        self.types = {
            TrainingInfoTable.trainings_per_week.name:int,
            TrainingInfoTable.workout.name: lambda x: {'похудение':['weight loss'],'функциональность':['functional'],'комплекс и накачка':['complex','pumping']}[x]
        }
        

    def _finish(self, user: User, message: types.Message) -> Message:
        blocks=self._db.get(BlockTable)
        exercises=self._db.get(ExerciseTable)
        programs=self._db.get(ProgramTable)

        person=self._db.get_one(TrainingInfoTable,user.id)

        creator=trainings_getter(person,programs,blocks,exercises)

        training=creator.get_training(6)
        print(training)

        finish_message=Message(0,'training_created',0,'')
        return finish_message
    


    def activate(self,user:User,message:types.Message)->Message:

        message_=super().activate(user,message)


        gender=self._db._get_one(UserInfoTable,user.id).gender
        info = self._db._get_one(self._table_class, user.id)
        info.gender=gender
        self._db._update()
        

        if message_ is None:
            self._db._delete(self._db._get_one(self.table_class,user.id))
            message_=super().activate(user,message)

        return message_