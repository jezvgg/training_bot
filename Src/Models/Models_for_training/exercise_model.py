from Src.Models.Models_for_training.abstract_model import abstract_reference
from Src.Models.Models_for_training.Enums.muscle_type import muscle_type
from Src.Models.Models_for_training.Enums.location_type import location_type
from Src.Models.Models_for_training.Enums.pattern_type import pattern_type
from dataclasses import dataclass
#пока должно быть поле текст, через которое генерим статью в тг


@dataclass
class Exercise_model(abstract_reference):
    __description:str=''
    __technique:str=''
    __recomendations:str=''
    __url_image:str=''
    __pattern:pattern_type=None
    __muscle:muscle_type=None
    __locations:location_type=None
    __is_circular:bool=False
    #ссылка на статью
    __link:str=None




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
    

