from DB.Tables import BaseTable
from sqlalchemy import Column, BigInteger, Boolean, JSON, String
from Src.Models import *
from Src.Enums import *


class BlockTable(BaseTable):
    __tablename__ = 'blocks'


    muscle=Column('muscle',String)
    exercises_criteria=Column('exercises_criteria',JSON)

    def __init__(self,muscle:str=None,exercises_criteria:dict[int, list[muscle_type,location_type,pattern_type]]=[]):
        self.muscle=muscle
        self.exercises_criteria=exercises_criteria


    def model(self):
        criteria={}
        for cur_day in self.exercises_criteria:
            criteria[cur_day]=[]
            for cur_criteria in self.exercises_criteria[cur_day]:
                criteria[cur_day].append([muscle_type(cur_criteria[0]),location_type(cur_criteria[1]),pattern_type(cur_criteria[2])])
        
        return Block_model('',muscle_type(self.muscle),criteria)
    
