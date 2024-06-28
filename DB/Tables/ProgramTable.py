from DB.Tables import BaseTable
from sqlalchemy import Column, BigInteger, Boolean, JSON
from Src.Models import *
from Src.Enums import *


class ProgramTable(BaseTable):
    __tablename__='Programs'

    id=Column('id',BigInteger,primary_key=True,autoincrement='auto',nullable=False)
    gender=Column('gender',Boolean)
    workout=Column('workout',JSON)
    trainings=Column('trainings',JSON)

    @staticmethod
    def build(model:Weekly_program_model):
        workout=[]
        for cur_type in model.workout:
            workout.append(cur_type.name)

        blocks={}
        for cur_day in model.trainings:
            blocks[cur_day]=[]
            for cur_block in model.trainings[cur_day]:
                blocks[cur_day].append(cur_block.muscle.name)
        
        return ProgramTable(model.name,model.is_male,workout,blocks)

    def __init__ (self,id:int,gender:bool=None,wokout:list[workout_type]=[],trainings:dict[int,Block_model]=[]):
        self.id=id
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


        
        return Weekly_program_model(self.id,self.gender,workout,trainings)
