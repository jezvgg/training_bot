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

        
        block_biceps=TrainingBlock("бицепс",arms,[[arms,location_type("дом"),pattern_type("накачка")],[arms,location_type("дом"),pattern_type("накачка")]])
        block_chest=TrainingBlock("бицепс",chest,[[chest,location_type("дом"),pattern_type("накачка")],[chest,location_type("дом"),pattern_type("накачка")]])



        program=TrainingProgramm('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=TrainingProgramm('пример 2',True,[spartan],{1:[block_biceps],2:[block_chest],5:[block_chest,block_biceps]})
        program_2=TrainingProgramm('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=TrainingProgramm('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=TrainingProgramm('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=TrainingPersonData('вася',True,3,[spartan])

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

        
        block_biceps=TrainingBlock("бицепс",arms,[[arms,location_type("дом"),pattern_type("локалка")],[arms,location_type("дом"),pattern_type("изолир")]])
        block_biceps_2=TrainingBlock("бицепс-одинарный",arms,[[arms,location_type("дом"),pattern_type("глобалка")]])
        block_chest=TrainingBlock("грудь",chest,[[chest,location_type("дом"),pattern_type("локалка")],[chest,location_type("дом"),pattern_type("глобалка")]])
        block_chest_2=TrainingBlock("грудь-одинарный",chest,[[chest,location_type("дом"),pattern_type("глобалка")]])


        program=TrainingProgramm('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=TrainingProgramm('пример 2',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_2=TrainingProgramm('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=TrainingProgramm('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=TrainingProgramm('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=TrainingPersonData('вася',True,3,[spartan])


        examp=trainings_getter([program,program_2,program_3,program_4,program_5],[block_biceps,block_chest,block_chest_2,block_biceps_2], [])
        fitting_program=examp.get_program(person)

        #действие
        chck=examp.get_blocks(fitting_program,2)

        #проверка
        assert len(chck[0])==1 and chck[0][0].name=='бицепс'
        assert len(chck[2])==1 and chck[2][0].name=='грудь'
        assert len(chck[4])==2 and chck[4][0].name=='грудь-одинарный' and chck[4][1].name=='бицепс-одинарный'

    
    def test_get_exercise(self):
        #подготовка
        chest=muscle_type('chest')
        arms=muscle_type('arms')

        
        kachat=workout_type('накачка')
        spartan=workout_type('spartan')

        
        block_biceps=TrainingBlock("бицепс",arms,[[arms,location_type("дом"),pattern_type("локалка")],[arms,location_type("зал"),pattern_type("глобалка")]])
        block_biceps_2=TrainingBlock("бицепс-одинарный",arms,[[arms,location_type("зал"),pattern_type("глобалка")]])
        block_chest=TrainingBlock("грудь",chest,[[chest,location_type("дом"),pattern_type("локалка")],[chest,location_type("дом"),pattern_type("глобалка")]])
        block_chest_2=TrainingBlock("грудь-одинарный",chest,[[chest,location_type("дом"),pattern_type("глобалка")]])


        program=TrainingProgramm('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=TrainingProgramm('пример 2',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_2=TrainingProgramm('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=TrainingProgramm('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=TrainingProgramm('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=TrainingPersonData('вася',True,3,[spartan])

        

        exer1=TrainingExercise('жим','',pattern_type('локалка'),muscle_type('chest'),location_type('дом'))
        exer2=TrainingExercise('махи','',pattern_type('глобалка'),muscle_type('chest'),location_type('дом'))
        exer3=TrainingExercise('гантели','',pattern_type('локалка'),muscle_type('arms'),location_type('дом'))
        exer4=TrainingExercise('станок','',pattern_type('глобалка'),muscle_type('arms'),location_type('дом'))
        exer5=TrainingExercise('станок 2','',pattern_type('глобалка'),muscle_type('arms'),location_type('зал'))



        examp=trainings_getter([program,program_2,program_3,program_4,program_5],[block_biceps,block_chest,block_chest_2,block_biceps_2],[exer1,exer2,exer3,exer4,exer5])
        fitting_program=examp.get_program(person)
        blocks=examp.get_blocks(fitting_program,2)


        #действие
        execises=examp.get_exercise(blocks)
        print(execises)
        #проверка
        for cur_key in execises.json().keys():
            assert len(execises[cur_key])==2 




    
    
    def test_get_training(self):
        #подготовка
        chest=muscle_type('chest')
        arms=muscle_type('arms')

        
        kachat=workout_type('накачка')
        spartan=workout_type('spartan')

        
        block_biceps=TrainingBlock("бицепс",arms,[[arms,location_type("дом"),pattern_type("локалка")],[arms,location_type("зал"),pattern_type("глобалка")]])
        block_biceps_2=TrainingBlock("бицепс-одинарный",arms,[[arms,location_type("зал"),pattern_type("глобалка")]])
        block_chest=TrainingBlock("грудь",chest,[[chest,location_type("дом"),pattern_type("локалка")],[chest,location_type("дом"),pattern_type("глобалка")]])
        block_chest_2=TrainingBlock("грудь-одинарный",chest,[[chest,location_type("дом"),pattern_type("глобалка")]])


        program=TrainingProgramm('пример',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_5=TrainingProgramm('пример 2',True,[spartan],{1:[block_biceps],3:[block_chest],5:[block_chest,block_biceps]})
        program_2=TrainingProgramm('не пример',True,[kachat],{1:None,3:None,5:None})
        program_3=TrainingProgramm('не пример',False,[spartan],{1:None,3:None,5:None})
        program_4=TrainingProgramm('не пример',True,[spartan],{1:None,3:None,5:None,6:None})
        person=TrainingPersonData('вася',True,3,[spartan])

        

        exer1=TrainingExercise('жим','',pattern_type('локалка'),muscle_type('chest'),location_type('дом'))
        exer2=TrainingExercise('махи','',pattern_type('глобалка'),muscle_type('chest'),location_type('дом'))
        exer3=TrainingExercise('гантели','',pattern_type('локалка'),muscle_type('arms'),location_type('дом'))
        exer4=TrainingExercise('станок','',pattern_type('глобалка'),muscle_type('arms'),location_type('дом'))
        exer5=TrainingExercise('станок 2','',pattern_type('глобалка'),muscle_type('arms'),location_type('зал'))



        examp=trainings_getter([program,program_2,program_3,program_4,program_5],[block_biceps,block_chest,block_chest_2,block_biceps_2],[exer1,exer2,exer3,exer4,exer5])
        


        #действие
        execises=examp.get_training(person, 2)


        #проверка
        for cur_key in execises.json().keys():
            print (execises[cur_key])
            assert len(execises[cur_key])==2

