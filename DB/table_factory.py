from DB.Tables import *
from Src.Models import *


class table_factory:
    '''
    Фабрика для конвертации моделей в таблицы БД.
    '''
    # К какой модели какую таблицу нужно использовать
    __map: dict[AbstractModel, BaseTable] = {
        Keyboard: KeyboardsTable,
        User: UserTable,
        Message: DialogueTable,
        Command: CommandsTable,
        TrainingBlock: BlockTable,
        TrainingExercise: ExerciseTable,
        TrainingPersonData: TrainingInfoTable,
        TrainingProgramm: ProgramTable,
        Feature: FeaturesTable
    }

    @staticmethod
    def get_type(model) -> type:
        if isinstance(model, type):
            return model

        return type(model)

    @classmethod
    def get(cls, model: AbstractModel):
        '''
        Получить класс таблицы соответсвющий моделе
        '''
        if cls.get_type(model) not in cls.__map.keys():
            raise Exception(
                f'Конвертация модели невозможна. Нет подходящей таблицы в фабрике. {cls.get_type(model)}')

        return cls.__map[cls.get_type(model)]

    @classmethod
    def create(cls, model: AbstractModel) -> BaseTable:
        '''
        Получить таблицу соответсвующую моделе
        '''
        # У этих таблиц соответственно должен быть фабричный метод от модели
        return cls.get(model).build(model)

    @classmethod
    def keys(cls):
        return list(cls.__map.keys())
