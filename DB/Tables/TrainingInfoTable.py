from DB.Tables import BaseTable
from sqlalchemy import Column, Boolean, JSON,Integer
from Src.Models import *
from Src.Enums import *

#сколько, где, тренировка
class TrainingInfoTable(BaseTable):
    __tablename__='trainings_info'

    id = Column("id", Integer, unique=True, primary_key=True,nullable=False)
    gender=Column('gender',Boolean)
    trainings_per_week=Column("trainings_per_week",Integer)
    workout=Column('workout',JSON)

    def __init__ (self,id:int,gender:bool=None,trainings_per_week:int=None,workout:list[workout_type]=None):
        self.id=id
        self.gender=gender
        self.trainings_per_week=trainings_per_week
        self.workout=workout


    def model(self):
        workout=[]
        for cur_workout in self.workout:
            workout.append(workout_type(cur_workout))
        return Person_training_model(id,self.gender,self.trainings_per_week,workout)