from DB.Tables import Base, BaseTable, MessagesTable
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine, inspect
from DB.table_factory import table_factory
from Src.Models import AbstractModel

# TODO: Сделать его синглтоном
class DBHelper:
    '''
    Класс для работы с БД
    '''
    session: Session
    engine: Engine

    def __init__(self, user: str, password: str, host: str, port: str, database: str):
        url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        # TODO: сделать проверку на наличие БД
        self.engine = create_engine(url, echo=False)

        Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def get(self, model: AbstractModel) -> list[BaseTable]:
        '''
        Получить таблицу данных соответствующую модели
        '''
        # TODO: Сделать проверку на наличие модели в фабрике
        return self.session.query(table_factory.get(model))


    def get_one(self, model: AbstractModel) -> BaseTable:
        '''
        Получить данные объекта из БД
        '''
        table = table_factory.get(model)
        return self.session.query(table).filter(table.id == model.id).one()


    def get_ones(self, model: AbstractModel) -> list[BaseTable]:
        '''
        Получить все данные всех обектов совпадающих с моделью
        '''
        table = table_factory.get(model)
        return self.session.query(table).filter(table.id == model.id).all()


    def get_models(self, model: AbstractModel) -> list[AbstractModel]:
        '''
        Получить модели из таблицы данных соответствующей модели
        '''
        return [table.model() for table in self.get(model)]


    def get_one_model(self, model: AbstractModel) -> AbstractModel:
        '''
        Получить модель из БД
        '''
        return self.get_one(model).model()


    def get_ones_models(self, model: AbstractModel) -> list[AbstractModel]:
        '''
        Получить все модели всех обектов совпадающих с моделью
        '''
        return [table.model() for table in self.get_ones(model)]
            
    # TODO: Сделать get с фильтрацией

    def add(self, model: AbstractModel):
        '''
        Добавление модели в БД
        '''
        table_object = table_factory.create(model)
        # TODO: проверка на корректность объекта и возможность его добавления
        self.session.add(table_object)
        self.session.commit()
        

