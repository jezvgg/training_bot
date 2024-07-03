from Src.Models import *
from Src.Enums.muscle_type import muscle_type
from Src.Prototypes import prototype


class block_prototype(prototype):
    '''прототип для фильтрации блоков по нужной мышце и количеству упражнений в блоке'''
    _data: list[TrainingBlock]


    def filter_block_on_day(self, muscle: muscle_type, amount_of_exercises: int):
        '''фильтрация блоков по типу мышцы и количеству упражнений
        Args:
            muscle - muscle_type мышца
            amount_of_exercises - количество упражнений'''
        result = []
        delta = 0

        while result == []:
            for cur_block in self._data:
                if cur_block.muscle.name==muscle.name and \
                amount_of_exercises - cur_block.count <= delta and \
                amount_of_exercises - cur_block.count >= 0:
                    result.append(cur_block)

            delta += 1

        return block_prototype(result)

