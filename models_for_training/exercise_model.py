from models_for_training.abstract_model import abstract_reference
from models_for_training.field_types.muscle_type import muscle_type
from models_for_training.field_types.location_type import location_type
from models_for_training.field_types.pattern_type import pattern_type

#пока должно быть поле текст, через которое генерим статью в тг

class Exercise_model(abstract_reference):
    __description:str=''
    __technique:str=''
    __recomendations:str=''
    __url_image:str=''
    __pattern:pattern_type=None
    __muscle:muscle_type=None
    __locations:location_type=None
    __is_circular:bool=False
    # __tolerance=0

    @property
    def description(self)->str:
        return self.__description

    @property
    def technique(self)->str:
        return self.__technique
    
    @property
    def recomendations(self)->str:
        return self.__recomendations
    
    @property
    def url_image(self)->str:
        return self.__url_image
    
    @property
    def pattern(self)->pattern_type:
        return self.__pattern

    @property
    def muscle(self)->muscle_type:
        return self.__muscle
    
    @property
    def locations(self)->location_type:
        return self.__locations
    
    @property
    def is_circular(self)->bool:
        return self.__is_circular
    
    @description.setter
    def description(self,value:str)->None:
        self.__description=value

    @technique.setter
    def technique(self,value:str)->None:
        self.__technique=value
    
    @recomendations.setter
    def recomendations(self,value:str)->None:
        self.__recomendations=value
    
    @url_image.setter
    def url_image(self,value:str)->None:
        self.__url_image=value
    
    @pattern.setter
    def pattern(self,value:pattern_type)->None:
        self.__pattern=value

    @muscle.setter
    def muscle(self,value:muscle_type)->None:
        self.__muscle=value
    
    @locations.setter
    def locations(self,value:location_type)->None:
        self.__locations=value
    
    @is_circular.setter
    def is_circular(self,value:bool)->None:
        self.__is_circular=value
    

    def __init__(self, name: str = "untituled") -> None:
        super().__init__(name)