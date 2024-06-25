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


        block1=Block_model('блок1',arms,[[],[],[]])
        block2=Block_model('блок2',arms,[[],[],[],[]])
        block3=Block_model('блок3',chest,[[],[],[]])
        block4=Block_model('блок4',hands,[[],[],[]])
        block5=Block_model('блок5',arms,[[],[],[]])

        prot=block_prototype([block1,block2,block3,block4,block5])

        #действие
        new=prot.filter_block_on_day(arms,3)

        #проверка
        assert len(new.data)==2
        assert new.sample()[0] in new.data