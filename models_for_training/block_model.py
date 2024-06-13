
from models_for_training.abstract_model import abstract_reference
from models_for_training.field_types.muscle_type import muscle_type
from models_for_training.field_types.location_type import location_type
from models_for_training.field_types.pattern_type import pattern_type

class  Block_model(abstract_reference):
    __muscle:muscle_type=None
    __exersices_criteria:list=[]


    @property
    def muscle(self)->muscle_type:
        return self.__muscle
    
    @property
    def exersices_criteria(self)->list:
        return self.__exersices_criteria
    
    @property 
    def count(self)->int:
        return len(self.__exersices_criteria)
    

    @muscle.setter
    def muscle(self,value:muscle_type)->None:
        self.__muscle=value

    def add_block(self)->None:
        if self.count<8:
            self.__exersices_criteria.append([])
        else:
            raise Exception("MAXIMUM VALUE OF TRAININGS PER WEEK IS 8")
    
    def add_critery(self,muscle:muscle_type,location:location_type,pattern:pattern_type,index:int=-1):
        self.__exersices_criteria[index]=[muscle,location,pattern]
