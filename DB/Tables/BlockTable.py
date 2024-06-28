from DB.Tables import BaseTable
from sqlalchemy import Column, Integer, JSON, String
from Src.Models import *
from Src.Enums import *


class BlockTable(BaseTable):
    __tablename__ = 'blocks'

    id=Column('id',Integer,primary_key=True,autoincrement='auto',nullable=False)
    muscle=Column('muscle',String)
    exercises_criteria=Column('exercises_criteria',JSON)

    @staticmethod
    def build(model:Block_model):
        criteria=[]

        for cur_criteria in model.exersices_criteria:
            criteria.append(cur_criteria[0].name,cur_criteria[1].name,cur_criteria[2].name)

        return BlockTable(model.name,model.muscle.name,criteria)

    def __init__(self,id:int,muscle:str=None,exercises_criteria:list[list[muscle_type,location_type,pattern_type]]=[]):
        self.id=id
        self.muscle=muscle
        self.exercises_criteria=exercises_criteria


    def model(self):
        criteria=[]

        for cur_criteria in self.exercises_criteria:
            criteria.append([muscle_type(cur_criteria[0]),location_type(cur_criteria[1]),pattern_type(cur_criteria[2])])
        
        return Block_model(id,muscle_type(self.muscle),criteria)
    
