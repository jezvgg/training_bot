from DB.Tables import BaseTable
from sqlalchemy import Column, Boolean, String
from Src.Models import *
from Src.Enums import *

class ExerciseTable(BaseTable):

    __tablename__='exercises'

    description=Column('description',String)
    technique=Column('technique',String)
    recomendations=Column('recomendations',String)
    url=Column('url',String)
    pattern=Column('pattern',String)
    muscle=Column('muscle',String)
    locations=Column('location',String)
    is_circular=Column('circular',Boolean)

    def __init__(self,description:str=None,technique:str=None,recomendations:str=None,url:str=None,pattern:pattern_type=None,muscle:muscle_type=None,locations:location_type=None,is_circular:bool=None):
        self.description=description
        self.technique=technique
        self.recomendations=recomendations
        self.url=url
        self.pattern=pattern
        self.muscle=muscle
        self.locations=locations
        self.is_circular=is_circular
    
    def model(self):


        return Exercise_model('',self.description,self.technique,self.recomendations,self.url,pattern_type(self.pattern),muscle_type(self.muscle),location_type(self.locations),self.is_circular)