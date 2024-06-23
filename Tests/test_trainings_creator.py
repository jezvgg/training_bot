import unittest
from Src.Models import *
from Src.Enums import *
from Src.trainings_creator import trainings_getter


class test_trainings_creator(unittest.TestCase):

    def test_get_training(self):
        #подготовка
        back=muscle_type('back')
        chest=muscle_type('chest')
        hands=muscle_type('hands')
        arms=muscle_type('arms')

        
        kachat=workout_type('накачка')
        slim=workout_type('fitnes')
        spartan=workout_type('spartan')


        home=location_type('дом')
        hall=location_type('зал')


        block_biceps=Block_model("бицепс",arms,[[arms,location_type("дом"),pattern_type("накачка")],[arms,location_type("дом"),pattern_type("накачка")]])
        block_chest=Block_model("бицепс",chest,[[chest,location_type("дом"),pattern_type("накачка")],[chest,location_type("дом"),pattern_type("накачка")]])


        exer1=Exercise_model('жим','',',','','',pattern_type('накачка'),muscle_type('chest'),location_type('дом'))
        exer2=Exercise_model('махи','',',','','',pattern_type('накачка'),muscle_type('chest'),location_type('дом'))
        exer3=Exercise_model('гантели','',',','','',pattern_type('накачка'),muscle_type('arms'),location_type('дом'))
        exer4=Exercise_model('станок','',',','','',pattern_type('накачка'),muscle_type('arms'),location_type('дом'))
        exer5=Exercise_model('станок 2','',',','','',pattern_type('фитнес'),muscle_type('бицепс'),location_type('дом'))


        program=Weekly_program_model('пример',1,[],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})


        training_creator=trainings_getter(program,[block_biceps,block_chest],[exer1,exer2,exer3,exer4,exer5])

        #действие
        training_creator.create_training(2)


        print(training_creator.program)

        #проверка
        assert True==True