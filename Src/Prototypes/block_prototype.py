from Src.Models import *
from Src.Enums.muscle_type import muscle_type
from Src.Prototypes import prototype
from random import sample


class block_prototype(prototype):
    '''прототип для фильтрации блоков по нужной мышце и количеству упражнений в блоке'''
    _data: list[TrainingBlock]


    def filter_block_on_day(self, muscle: muscle_type, amount_of_exercises: int):
        '''фильтрация блоков по типу мышцы и количеству упражнений
        Args:
            muscle - muscle_type мышца
            amount_of_exercises - количество упражнений'''
        result = []


        for cur_block in self._data:
            if cur_block.muscle.name==muscle.name and \
            (cur_block.count-amount_of_exercises)<=2:
                result.append(cur_block)

        return block_prototype(result)
