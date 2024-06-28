import unittest
from Src.Models.Models_for_training.exercise_model import TrainingExercise
from Src.Models.Models_for_training.block_model import TrainingBlock
from Src.Models.Models_for_training.person_training_model import TrainingPersonData
from Src.Models.Models_for_training.program_model import TrainingProgramm
from Src.Enums.pattern_type import pattern_type
from Src.Enums.muscle_type import muscle_type
from Src.Enums.location_type import location_type
from Src.Enums.workout_type import workout_type
from Src.Prototypes.training_prototype import training_prototype

class test_training_prototype(unittest.TestCase):

    def test_choose_program(self):
        #подготовка
        kachat=workout_type('kachat')
        slim=workout_type('fitnes')
        spartan=workout_type('spartan')
        
        baki=TrainingPersonData('baki',True,5,[workout_type('kachat')])
        joseph=TrainingPersonData('Joseph',True,3,[spartan])
        kama=TrainingPersonData('kama',True,3,[spartan])
        jolyn=TrainingPersonData('Jolyne',False,3,[spartan])
        ky=TrainingPersonData("Ky",True,3,[slim])


        joestar=TrainingProgramm("Joestar",True,[spartan],{1:None,3:None,5:None})
        pula=TrainingProgramm("Pula",True,[spartan],{1:None,2:None,3:None})
        hanma=TrainingProgramm("Hanma",True,[kachat],{1:None,2:None,3:None,4:None,5:None})
        kujo=TrainingProgramm("Kujo",False,[spartan],{1:None,3:None,5:None})
        kiske=TrainingProgramm("Kiske",True,[slim],{1:None,3:None,5:None})

        #действие
        prot=training_prototype([joestar,pula,hanma,kujo,kiske])
        battle_tendency=prot.filter_person_training_model(joseph)
        grappler=prot.filter_person_training_model(baki)
        schaa=prot.filter_person_training_model(kama)
        stone_ocean=prot.filter_person_training_model(jolyn)
        gear=prot.filter_person_training_model(ky)



        #проверка
        print(f'joseph:{battle_tendency.data}')
        assert battle_tendency.sample() is not None
        print(f'sample:{battle_tendency.sample()} ')
        assert len(battle_tendency.data)==2

        print(f'kama:{schaa.data}')
        assert len(schaa.data)==2

        print(f'baki:{grappler.data}')
        assert len(grappler.data)==1 
        assert grappler.data[0]==hanma

        print(f'jolyn:{stone_ocean.data}')
        assert len(stone_ocean.data)==1 
        assert stone_ocean.data[0]==kujo

        print(f'Ky:{gear.data}')
        assert len(gear.data)==1
        assert gear.data[0]==kiske


