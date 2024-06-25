import unittest
from Src.Models import *
from Src.Prototypes.exercise_prototype import exersise_prototype
from Src.Enums.muscle_type import muscle_type
from Src.Enums.pattern_type import pattern_type
from Src.Enums.location_type import location_type

class test_exersise_prototype(unittest.TestCase):

    def test_prototype_work(self):
        #подготовка
        block=Block_model('руки',muscle_type('бицепс'),[[muscle_type('бицепс'),location_type('дом'),pattern_type('накачка')]])
        exer1=Exercise_model('жим','',',','','',pattern_type('накачка'),muscle_type('грудь'),location_type('дом'))
        exer2=Exercise_model('махи','',',','','',pattern_type('фитнес'),muscle_type('бицепс'),location_type('зал'))
        exer3=Exercise_model('гантели','',',','','',pattern_type('накачка'),muscle_type('бицепс'),location_type('дом'))
        exer4=Exercise_model('станок','',',','','',pattern_type('накачка'),muscle_type('бицепс'),location_type('зал'))
        exer5=Exercise_model('станок 2','',',','','',pattern_type('фитнес'),muscle_type('бицепс'),location_type('дом'))

        print(block.exersices_criteria)
        #действие
        prot=exersise_prototype([exer1,exer2,exer3,exer4,exer5])
        new=prot.filter_exercises_criteria(block.exersices_criteria[0])


        #проверка
        print(new.data)
        assert len(new.data)==1
        assert new.sample()[0].name=='гантели'
        assert new.data[0].name=='гантели'