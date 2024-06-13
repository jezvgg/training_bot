import unittest 
from models_for_training.exercise_model import Exercise_model
from models_for_training.block_model import Block_model
from models_for_training.person_training_model import person_training_model
from models_for_training.program_model import Weekly_program_model
from models_for_training.field_types.pattern_type import pattern_type
from models_for_training.field_types.muscle_type import muscle_type
from models_for_training.field_types.location_type import location_type
from models_for_training.field_types.workout_type import workout_type

class test_models_for_training(unittest.TestCase):

    def test_exercise_model(self):
        #подготовка
        name='name'
        desc='some_description_test'
        tech='some_technique_test'
        recs='recomendations'
        url='some_url_mes'
        pat=pattern_type('some_pattern_test')
        mus=muscle_type('some_muscle')
        loc=location_type('name')
        circ=True
        exer=Exercise_model()






        #действие
        exer.description=desc
        exer.url_image=url
        exer.recomendations=recs
        exer.technique=tech
        exer.is_circular=circ
        exer.locations=loc
        exer.muscle=mus
        exer.name=name
        exer.pattern=pat


        #проверка
        assert exer.name==name
        assert exer.description==desc
        assert exer.is_circular==True
        assert exer.url_image==url
        assert exer.recomendations==recs
        assert exer.technique==tech
        assert exer.muscle==mus
        assert exer.locations==loc
        assert exer.pattern==pat

    def test_block_model(self):
        #подготовка
        name='name'
        mus=muscle_type('some_muscle')
        mus2=muscle_type('some_muscle_number 2')
        pat=pattern_type('some_pattern_test')
        pat2=pattern_type('some_pattern_test2')
        loc=location_type('some_location')
        loc2=location_type('some_location_2')
        bl=Block_model()
        

        #действие
        bl.name=name
        bl.muscle=mus
        bl.add_block()
        bl.add_critery(mus,loc,pat)
        bl.add_block()
        bl.add_critery(mus2,loc2,pat2)
        bl.add_block()
        bl.add_critery(mus,loc2,pat)

        #проверка
        assert bl.name==name
        assert bl.count==3
        for x in bl.exersices_criteria:
            assert len(x)==3

            print(x[0].name,x[1].name,x[2].name)
        assert bl.exersices_criteria[0][0].name==mus.name
        assert bl.exersices_criteria[0][1].name==loc.name
        assert bl.exersices_criteria[0][2].name==pat.name

        assert bl.exersices_criteria[1][0].name==mus2.name
        assert bl.exersices_criteria[1][1].name==loc2.name
        assert bl.exersices_criteria[1][2].name==pat2.name

        assert bl.exersices_criteria[2][0].name==mus.name
        assert bl.exersices_criteria[2][1].name==loc2.name
        assert bl.exersices_criteria[2][2].name==pat.name

    def test_block_overflow(self):
        #подготовка
        bl=Block_model()
        

        #действие
        for i in range(8):
            bl.add_block()


        #проверка 
        try:
            bl.add_block()
            assert False==True
        except:
            assert True==True


    def test_person_training_model(self):
        #подготовка
        name='some_name'
        male=True
        workout=workout_type('workout 1')
        workout_2=workout_type('workout 2')
        workouts_per_week=3
        tr=person_training_model()

        #действие
        tr.is_male=male
        tr.name=name
        tr.trains_per_week=workouts_per_week
        tr.add_workout(workout)
        tr.add_workout(workout_2)

        #проверка
        assert tr.is_male==male
        assert tr.name==name
        assert tr.trains_per_week==workouts_per_week
        assert tr.workout==[workout,workout_2]
        tr.clear_workout()
        assert tr.workout==[]



    def test_person_training_model_overflow(self):
        #подготовка
        name='some_name'
        male=True
        workout=workout_type('workout 1')
        workout_2=workout_type('workout 2')
        workouts_per_week=8
        tr=person_training_model()

        #действие
        tr.is_male=male
        tr.name=name
        tr.add_workout(workout)
        tr.add_workout(workout_2)


        
        #проверка
        try:
            tr.trains_per_week=workouts_per_week
            assert True==False
        except:
            assert True==True



    def test_weekly_program_model(self):
        #подготовка
        pr=Weekly_program_model()
        name='some_name'
        workout=workout_type('workout 1')
        workout_2=workout_type('workout 2')
        male=True

        mus=muscle_type('some_muscle')
        mus2=muscle_type('some_muscle_number 2')
        pat=pattern_type('some_pattern_test')
        pat2=pattern_type('some_pattern_test2')
        loc=location_type('some_location')
        loc2=location_type('some_location_2')
        bl=Block_model()
        
        bl.name=name
        bl.muscle=mus
        bl.add_block()
        bl.add_critery(mus,loc,pat)
        bl.add_block()
        bl.add_critery(mus2,loc2,pat2)
        bl.add_block()
        bl.add_critery(mus,loc2,pat)


        #действие
        pr.is_male=male
        pr.name=name
        pr.add_workout_type(workout)
        pr.add_workout_type(workout_2)
        pr.add_block(bl,1)
        pr.add_block(bl,1)
        pr.add_block(bl,4)


        #проверка
        assert pr.name==name
        assert pr.is_male==male
        assert pr.workouts_per_week==2
        assert pr.workout==[workout,workout_2]
        assert pr.trainings[1]==[bl,bl]
        assert pr.trainings[4]==[bl]



    def test_weekly_program_model_overflow(self):
        #подготовка
        pr=Weekly_program_model()
        name='some_name'
        workout=workout_type('workout 1')
        workout_2=workout_type('workout 2')
        male=True

        mus=muscle_type('some_muscle')
        mus2=muscle_type('some_muscle_number 2')
        pat=pattern_type('some_pattern_test')
        pat2=pattern_type('some_pattern_test2')
        loc=location_type('some_location')
        loc2=location_type('some_location_2')
        bl=Block_model()
        
        bl.name=name
        bl.muscle=mus
        bl.add_block()
        bl.add_critery(mus,loc,pat)
        bl.add_block()
        bl.add_critery(mus2,loc2,pat2)
        bl.add_block()
        bl.add_critery(mus,loc2,pat)


        #действие
        pr.is_male=male
        pr.name=name
        pr.add_workout_type(workout)
        pr.add_workout_type(workout_2)
        pr.add_block(bl,1)
        pr.add_block(bl,1)
        pr.add_block(bl,4)


        #проверкка
        try: 
            pr.add_block(bl,7)
            assert False==True
        except:
            assert True==True
