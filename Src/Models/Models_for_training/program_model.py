from Src.Models.Models_for_training.abstract_model import abstract_reference
from Src.Models.Models_for_training.block_model import Block_model
from Src.Models.Models_for_training.Enums.workout_type import workout_type
from dataclasses import dataclass, field

@dataclass
class Weekly_program_model(abstract_reference):
    __is_male:bool=True
    __workout:list[workout_type]=field(default_factory=list[workout_type])
    __trainings:dict[int:list[Block_model]]=field(default_factory=dict[int:list[Block_model]])



    @property
    def is_male(self)->bool:
        return self.__is_male

    @property
    def workout(self)->list[workout_type]:
        return self.__workout
    
    @property 
    def workouts_per_week(self)->int:
        return len(list(self.__trainings.keys()))
    
    @property
    def trainings(self)->dict[int:list[Block_model]]:
        return self.__trainings
    
    @is_male.setter
    def is_male(self,value:bool)->None:
        self.__is_male=value

    def add_workout_type(self,value:workout_type)->None:
        self.__workout.append(value)



    def add_block(self,block:Block_model,day:int=1)->None:
        #TODO инвертировать логику
        if day >0 and day<6:
            if day in self.__trainings.keys():

                self.__trainings[day].append(block)
            else:
                self.__trainings[day]=[block]
        else:
            raise Exception("Day must be from 1 to 5")