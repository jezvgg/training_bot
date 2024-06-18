from Src.Models.Models_for_training.Enums.location_type import location_type
from Src.Models.Models_for_training.Enums.pattern_type import pattern_type
from Src.Models.Models_for_training.Enums.workout_type import workout_type
from Src.Models.Models_for_training.Enums.muscle_type import muscle_type
from Src.Models.Models_for_training.exercise_model import Exercise_model
from Src.Models.Models_for_training.block_model import Block_model

class test_data_creator:
    def create_test_data(self):
        muscles=test_data_creator._create_test_muscles()
        locs=test_data_creator._create_test_locations()
        pats=test_data_creator._create_test_patterns()
        exers=test_data_creator._create_test_exercises()
        blocks=test_data_creator._create_test_blocks()
        for index in range(exers):
            exers[index].muscle=muscles[index]
            exers[index].locations=locs[index%2]
            exers[index].pattern=pats[index%3]

        


    @staticmethod
    def _create_test_blocks():
        block_a=Block_model('BLOCK A')
        block_b=Block_model('BLOCK B')
        block_c=Block_model('BLOCK C')
        block_d=Block_model('BLOCK D')
        
        res=[block_a,block_b,block_c,block_d]

        for i in range(2):
            for j in range(4):
                res[j].add_block()
        
        res[1].add_block()
        res[1].add_block()
        res[3].add_block()
        res[3].add_block()

        return res
        

    @staticmethod
    def _create_test_exercises():
        name_a='exersize A'
        name_b='exersize B'
        name_c='exersize C'
        name_d='exersize D'
        name_e='exersize E'

        model_a=Exercise_model(name_a)
        model_b=Exercise_model(name_b)
        model_c=Exercise_model(name_c)
        model_d=Exercise_model(name_d)
        model_e=Exercise_model(name_e)

        return [model_a,model_b,model_c,model_d,model_e]


    @staticmethod
    def _create_test_programs():
        pass

    @staticmethod
    def _create_test_muscles():
        muscle_a=muscle_type('muscle A')
        muscle_b=muscle_type('muscle B')
        muscle_c=muscle_type('muscle C')
        muscle_d=muscle_type('muscle D')
        muscle_e=muscle_type('muscle E')


        return [muscle_a,muscle_b,muscle_c,muscle_d,muscle_e]
    
    @staticmethod
    def _create_test_patterns():
        pattern_a=pattern_type('pattern_a A')
        pattern_b=pattern_type('pattern_a B')
        pattern_c=pattern_type('pattern_a C')


        return [pattern_a,pattern_b,pattern_c]
    
    @staticmethod
    def _create_test_locations():
        loc1=location_type("home")
        loc2=location_type('hall')

        return[loc1,loc2]