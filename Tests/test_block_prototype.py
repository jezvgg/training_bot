import unittest
from Src.Models import *
from Src.Prototypes import *
from Src.Enums import *

class test_block_prototype(unittest.TestCase):

    def test_prototype_work(self):
        #подготовка
        back=muscle_type('back')
        chest=muscle_type('chest')
        hands=muscle_type('hands')
        arms=muscle_type('arms')


        block1=TrainingBlock('блок1',arms,[[],[],[]])
        block2=TrainingBlock('блок2',arms,[[],[],[],[]])
        block3=TrainingBlock('блок3',chest,[[],[],[]])
        block4=TrainingBlock('блок4',hands,[[],[],[]])
        block5=TrainingBlock('блок5',arms,[[],[],[]])

        prot=block_prototype([block1,block2,block3,block4,block5])

        #действие
        new=prot.filter_block_on_day(arms,3)

        #проверка
        assert len(new.data)==2
        assert new.sample() in new.data