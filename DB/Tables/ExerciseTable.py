from DB.Tables import BaseTable
from sqlalchemy import Column, Boolean, String, Integer
from Src.Models import *
from Src.Enums import *


class ExerciseTable(BaseTable):

    __tablename__ = 'exercises'
    id = Column('id', Integer, primary_key=True,
                autoincrement='auto', nullable=False)
    description = Column('description', String)
    technique = Column('technique', String)
    recomendations = Column('recomendations', String)
    url = Column('url', String)
    pattern = Column('pattern', String)
    muscle = Column('muscle', String)
    locations = Column('location', String)
    is_circular = Column('circular', Boolean)


    @staticmethod
    def build(model: Exercise_model):
        return ExerciseTable(model.name, model.description, model.technique, 
                            model.recomendations, model.url_image, model.pattern.name, 
                            model.muscle.name, model.locations.name, model.is_circular)


    def __init__(self, id: int, description: str = None, technique: str = None, recomendations: str = None, url: str = None, pattern: pattern_type = None, muscle: muscle_type = None, locations: location_type = None, is_circular: bool = None):
        self.id = id
        self.description = description
        self.technique = technique
        self.recomendations = recomendations
        self.url = url
        self.pattern = pattern
        self.muscle = muscle
        self.locations = locations
        self.is_circular = is_circular


    def model(self):
        return Exercise_model(self.id, self.description, self.technique, self.recomendations, 
                            self.url, pattern_type(self.pattern), muscle_type(self.muscle), 
                            location_type(self.locations), self.is_circular)
