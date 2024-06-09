from models_for_training.abstract_model import abstract_reference
from models_for_training.block_model import Block_model
from models_for_training.field_types.workout_type import workout_type

class Weekly_program_model(abstract_reference):
    __is_male:bool=True
    __workout:list=[]
    __trainings:list=[]



    @property
    def is_male(self)->bool:
        return self.__is_male
    

    @property
    def workout(self)->list:
        return self.__workout
    
    @property 
    def workouts_per_week(self)->int:
        return len(self.__trainings)
    
    @property
    def trainings(self)->list:
        return self.__trainings
    
    @is_male.setter
    def is_male(self,value:bool)->None:
        self.__is_male=value

    def add_workout_type(self,value:workout_type)->None:
        self.__workout.append(value)

    def add_training(self)->None:
        if self.workouts_per_week<5:
            self.__trainings.append([])
        else:
            raise Exception("MAXIMUM VALUE OF TRAININGS PER WEEK IS 5")

    def add_block(self,block:Block_model,index:int=-1)->None:
        try:
            self.__trainings[index].append(block)
        
        except Exception as ex:
            print(f'error {ex} occured')
