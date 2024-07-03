from Src.Models.training_base import training_base
from Src.Enums.muscle_type import muscle_type
from Src.Enums.location_type import location_type
from Src.Enums.pattern_type import pattern_type
from dataclasses import dataclass
# пока должно быть поле текст, через которое генерим статью в тг


@dataclass
class TrainingExercise(training_base):
    '''модель упражнения'''
    __ex_name: str = ''
    __pattern: pattern_type = None
    __muscle: muscle_type = None
    __locations: location_type = None
    __is_circular: bool = False
    __link: str = None


    def json(self):
        return {'name':self.ex_name,
                'pattern': self.pattern.name,
                'muscle': self.muscle.name,
                'locations': self.locations.name,
                'is_circular': self.is_circular,
                'link': self.link}


    @property
    def ex_name(self) -> str:
        '''описание упражнения'''
        return self.__ex_name

    @property
    def pattern(self) -> pattern_type:
        '''тип работы мышцы'''
        return self.__pattern

    @property
    def muscle(self) -> muscle_type:
        '''мышца'''
        return self.__muscle

    @property
    def locations(self) -> location_type:
        '''место'''
        return self.__locations

    @property
    def is_circular(self) -> bool:
        '''является ли циклической'''
        return self.__is_circular

    @ex_name.setter
    def ex_name(self, value: str) -> None:
        self.__ex_name = value

    @pattern.setter
    def pattern(self, value: pattern_type) -> None:
        self.__pattern = value

    @muscle.setter
    def muscle(self, value: muscle_type) -> None:
        self.__muscle = value

    @locations.setter
    def locations(self, value: location_type) -> None:
        self.__locations = value

    @is_circular.setter
    def is_circular(self, value: bool) -> None:
        self.__is_circular = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value: str) -> None:
        self.__link = value
