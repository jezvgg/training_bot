from Src.Models import *
from Src.Enums.muscle_type import muscle_type
from Src.Prototypes import prototype
from random import sample


class block_prototype(prototype):
    '''прототип для фильтрации блоков по нужной мышце и количеству упражнений в блоке'''
    _data: list[Block_model]


    def filter_block_on_day(self, muscle: muscle_type, amount_of_exercises: int):
        '''фильтрация'''
        result = []

        for cur_block in self._data:
            if cur_block.muscle.name == muscle.name and \
                    cur_block.count == amount_of_exercises:
                result.append(cur_block)

        return block_prototype(result)

