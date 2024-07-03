from DB.Tables import BaseTable
from sqlalchemy import Column, Boolean, String, Integer
from Src.Models import *
from Src.Enums import *


class ExerciseTable(BaseTable):
    __tablename__ = 'exercises'

    id = Column('id', Integer, primary_key=True,
                autoincrement='auto', nullable=False)
    name = Column('name', String)
    pattern = Column('pattern', String)
    muscle = Column('muscle', String)
    locations = Column('location', String)
    is_circular = Column('circular', Boolean)
    link = Column('link', String)


    @staticmethod
    def build(model: TrainingExercise):
        return ExerciseTable(model.name, model.ex_name, model.pattern.name, 
                            model.muscle.name, model.locations.name, model.is_circular, model.link)


    def __init__(self, id: int, name: str = None, pattern: pattern_type = None, muscle: muscle_type = None, locations: location_type = None, is_circular: bool = None):
        self.id = id
        self.name = name
        self.pattern = pattern
        self.muscle = muscle
        self.locations = locations
        self.is_circular = is_circular


    def model(self):
        return TrainingExercise(self.id, self.name, pattern_type(self.pattern), 
                                muscle_type(self.muscle), location_type(self.locations), 
                                self.is_circular, self.link)
