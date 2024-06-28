from DB.Tables import BaseTable
from sqlalchemy import Column, Boolean, JSON, BigInteger, Integer
from Src.Models import *
from Src.Enums import *


class TrainingInfoTable(BaseTable):
    __tablename__ = 'trainings_info'

    training_id = Column('id', Integer, unique=True,
                        primary_key=True, nullable=False)
    id = Column("user_id", BigInteger)
    gender = Column('gender', Boolean)
    trainings_per_week = Column("trainings_per_week", Integer)
    workout = Column('workout_type', JSON)
    training = Column('training', JSON)


    @staticmethod
    def build(model: TrainingPersonData):
        workouts = []
        for cur_workout in model.workout:
            workouts.append(cur_workout.name)
        return TrainingInfoTable(model.name, model.gender, model.trains_per_week, workouts)


    def __init__(self, id: int, gender: bool = None, trainings_per_week: int = None, workout: list[workout_type] = None, training: dict = None):
        self.id = id
        self.gender = gender
        self.trainings_per_week = trainings_per_week
        self.workout = workout
        self.training = training


    def model(self):
        workout = []
        for cur_workout in self.workout:
            workout.append(workout_type(cur_workout))
        return TrainingPersonData(id, self.gender, self.trainings_per_week, workout)
