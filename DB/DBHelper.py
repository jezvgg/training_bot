from DB.Tables import Base, BaseTable
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine
from DB.table_factory import table_factory
from Src.Models import AbstractModel

# TODO: Сделать его синглтоном
class DBHelper:
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


    # TODO: Сделать get с фильтрацией
    # TODO: Сделать получение сразу моделей
    


    def add(self, model: AbstractModel):
        '''
        Добавление модели в БД
        '''
        table_object = table_factory.create(model)
        # TODO: проверка на корректность объекта и возможность его добавления
        self.session.add(table_object)
        self.session.commit()
        

