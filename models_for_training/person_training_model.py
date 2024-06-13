#не юсер, а друге имя

from models_for_training.abstract_model import abstract_reference
from models_for_training.field_types.workout_type import workout_type


class person_training_model(abstract_reference):
    __is_male:bool=False
    __trains_per_week:int=0
    __workout:list=[]


    def __init__(self, name: str = "untituled") -> None:
        super().__init__(name)

    @property
    def workout(self)->list[workout_type]:
        return self.__workout
    
    @property
    def is_male(self)->bool:
        return self.__is_male
    
    @property 
    def trains_per_week(self)->int:
        return self.__trains_per_week
    
    @is_male.setter
    def is_male(self,value:bool)->None:
        self.__is_male=value
    
    @trains_per_week.setter
    def trains_per_week(self,value:int)->None:
        if value>0 and value <6:
            self.__trains_per_week=value
        else:
            raise Exception("value must be between 1 and 5")
        
    def add_workout(self,value:workout_type)->None:
        self.__workout.append(value)

    def clear_workout(self)->None:
        self.__workout=[]


