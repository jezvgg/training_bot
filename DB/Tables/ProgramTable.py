from DB.Tables import BaseTable
from sqlalchemy import Column, BigInteger, Boolean, JSON
from Src.Models import *
from Src.Enums import *


class ProgramTable(BaseTable):
    __tablename__='Programs'

    id=Column('id',BigInteger,primary_key=True,autoincrement='auto')
    gender=Column('gender',Boolean)
    workout=Column('workout',JSON)
    trainings=Column('trainings',JSON)

    def __init__ (self,gender:bool=None,wokout:list[workout_type]=[],trainings:dict[int,Block_model]=[]):
        self.gender=gender
        self.workout=wokout
        self.trainings=trainings
        
    def model(self):
        workout=[]
        trainings={}
        
        for cur_name in self.workout:
            workout.append(workout_type(cur_name))
        
        for cur_day in self.trainings:
            trainings[cur_day]=[]

            for cur_block in self.trainings[cur_day]:
                trainings[cur_day].append(Block_model('',muscle_type(cur_block)))


        
        result=Weekly_program_model('',self.gender,workout,trainings)
