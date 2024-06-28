import unittest
from Src.Models import *
from Src.Enums import *
from Src.trainings_creator import trainings_getter


class test_trainings_creator(unittest.TestCase):

    def test_get_program(self):
        #подготовка
        chest=muscle_type('chest')
        arms=muscle_type('arms')

        
        kachat=workout_type('накачка')
        spartan=workout_type('spartan')

        
        block_biceps=Block_model("бицепс",arms,[[arms,location_type("дом"),pattern_type("накачка")],[arms,location_type("дом"),pattern_type("накачка")]])
        block_chest=Block_model("бицепс",chest,[[chest,location_type("дом"),pattern_type("накачка")],[chest,location_type("дом"),pattern_type("накачка")]])



        program=Weekly_program_model('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=Weekly_program_model('пример 2',True,[spartan],{1:[block_biceps],2:[block_chest],5:[block_chest,block_biceps]})
        program_2=Weekly_program_model('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=Weekly_program_model('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=Weekly_program_model('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=Person_training_model('вася',True,3,[spartan])

        #действие
        examp=trainings_getter([program,program_2,program_3,program_4,program_5], [], [])
        chck=examp.get_program(person)

        #проверка
        print(chck.name)
        assert chck.name=='пример' or chck.name=='пример 2'


    def test_get_blocks(self):
        #подготовка
        chest=muscle_type('chest')
        arms=muscle_type('arms')

        
        kachat=workout_type('накачка')
        spartan=workout_type('spartan')

        
        block_biceps=Block_model("бицепс",arms,[[arms,location_type("дом"),pattern_type("локалка")],[arms,location_type("дом"),pattern_type("изолир")]])
        block_biceps_2=Block_model("бицепс-одинарный",arms,[[arms,location_type("дом"),pattern_type("глобалка")]])
        block_chest=Block_model("грудь",chest,[[chest,location_type("дом"),pattern_type("локалка")],[chest,location_type("дом"),pattern_type("глобалка")]])
        block_chest_2=Block_model("грудь-одинарный",chest,[[chest,location_type("дом"),pattern_type("глобалка")]])


        program=Weekly_program_model('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=Weekly_program_model('пример 2',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_2=Weekly_program_model('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=Weekly_program_model('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=Weekly_program_model('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=Person_training_model('вася',True,3,[spartan])


        examp=trainings_getter([program,program_2,program_3,program_4,program_5],[block_biceps,block_chest,block_chest_2,block_biceps_2], [])
        fitting_program=examp.get_program(person)

        #действие
        chck=examp.get_blocks(fitting_program,2)

        #проверка
        assert len(chck[1])==1 and chck[1][0].name=='бицепс'
        assert len(chck[3])==1 and chck[3][0].name=='грудь'
        assert len(chck[5])==2 and chck[5][0].name=='грудь-одинарный' and chck[5][1].name=='бицепс-одинарный'

    
    def test_get_exercise(self):
        #подготовка
        chest=muscle_type('chest')
        arms=muscle_type('arms')

        
        kachat=workout_type('накачка')
        spartan=workout_type('spartan')

        
        block_biceps=Block_model("бицепс",arms,[[arms,location_type("дом"),pattern_type("локалка")],[arms,location_type("зал"),pattern_type("глобалка")]])
        block_biceps_2=Block_model("бицепс-одинарный",arms,[[arms,location_type("зал"),pattern_type("глобалка")]])
        block_chest=Block_model("грудь",chest,[[chest,location_type("дом"),pattern_type("локалка")],[chest,location_type("дом"),pattern_type("глобалка")]])
        block_chest_2=Block_model("грудь-одинарный",chest,[[chest,location_type("дом"),pattern_type("глобалка")]])


        program=Weekly_program_model('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=Weekly_program_model('пример 2',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_2=Weekly_program_model('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=Weekly_program_model('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=Weekly_program_model('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=Person_training_model('вася',True,3,[spartan])

        

        exer1=Exercise_model('жим','',',','','',pattern_type('локалка'),muscle_type('chest'),location_type('дом'))
        exer2=Exercise_model('махи','',',','','',pattern_type('глобалка'),muscle_type('chest'),location_type('дом'))
        exer3=Exercise_model('гантели','',',','','',pattern_type('локалка'),muscle_type('arms'),location_type('дом'))
        exer4=Exercise_model('станок','',',','','',pattern_type('глобалка'),muscle_type('arms'),location_type('дом'))
        exer5=Exercise_model('станок 2','',',','','',pattern_type('глобалка'),muscle_type('arms'),location_type('зал'))



        examp=trainings_getter([program,program_2,program_3,program_4,program_5],[block_biceps,block_chest,block_chest_2,block_biceps_2],[exer1,exer2,exer3,exer4,exer5])
        fitting_program=examp.get_program(person)
        blocks=examp.get_blocks(fitting_program,2)


        #действие
        execises=examp.get_exercise(blocks)

        #проверка
        for cur_key in execises.keys():
            assert len(execises[cur_key])==2




    
    
    def test_get_training(self):
        #подготовка
        chest=muscle_type('chest')
        arms=muscle_type('arms')

        
        kachat=workout_type('накачка')
        spartan=workout_type('spartan')

        
        block_biceps=Block_model("бицепс",arms,[[arms,location_type("дом"),pattern_type("локалка")],[arms,location_type("зал"),pattern_type("глобалка")]])
        block_biceps_2=Block_model("бицепс-одинарный",arms,[[arms,location_type("зал"),pattern_type("глобалка")]])
        block_chest=Block_model("грудь",chest,[[chest,location_type("дом"),pattern_type("локалка")],[chest,location_type("дом"),pattern_type("глобалка")]])
        block_chest_2=Block_model("грудь-одинарный",chest,[[chest,location_type("дом"),pattern_type("глобалка")]])


        program=Weekly_program_model('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=Weekly_program_model('пример 2',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_2=Weekly_program_model('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=Weekly_program_model('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=Weekly_program_model('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=Person_training_model('вася',True,3,[spartan])

        

        exer1=Exercise_model('жим','',',','','',pattern_type('локалка'),muscle_type('chest'),location_type('дом'))
        exer2=Exercise_model('махи','',',','','',pattern_type('глобалка'),muscle_type('chest'),location_type('дом'))
        exer3=Exercise_model('гантели','',',','','',pattern_type('локалка'),muscle_type('arms'),location_type('дом'))
        exer4=Exercise_model('станок','',',','','',pattern_type('глобалка'),muscle_type('arms'),location_type('дом'))
        exer5=Exercise_model('станок 2','',',','','',pattern_type('глобалка'),muscle_type('arms'),location_type('зал'))



        examp=trainings_getter([program,program_2,program_3,program_4,program_5],[block_biceps,block_chest,block_chest_2,block_biceps_2],[exer1,exer2,exer3,exer4,exer5])
        


        #действие
        execises=examp.get_training(person, 2)


        #проверка
        for cur_key in execises.keys():
            print (execises[cur_key])
            assert len(execises[cur_key])==2

