from DB.Tables import Base, BaseTable
from sqlalchemy.orm import sessionmaker, Session, Query
from sqlalchemy import create_engine, Engine
from DB.table_factory import table_factory
from Src.Models import AbstractModel


class DBHelper(object):
    '''
    Класс для работы с БД
    '''
    session: Session
    engine: Engine

    # TODO: Добавить in

    def __init__(self, user: str, password: str, host: str, port: str, database: str):
        url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        # TODO: сделать проверку на наличие БД
        self.engine = create_engine(url, echo=False)

        Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBHelper, cls).__new__(cls)
        return cls.instance


    def get(self, model: AbstractModel) -> Query[BaseTable]:
        '''
        Получить таблицу данных соответствующую модели
        '''
        # TODO: Сделать проверку на наличие модели в фабрике
        return self.session.query(table_factory.get(model))


    def get_one(self, model: AbstractModel, id: int) -> BaseTable:
        '''
        Получить данные объекта из БД
        '''
        table = table_factory.get(model)
        return self.session.query(table).filter(table.id == id).one()


    def get_ones(self, model: AbstractModel, id: int) -> list[BaseTable]:
        '''
        Получить все данные всех обектов совпадающих с моделью
        '''
        table = table_factory.get(model)
        return self.session.query(table).filter(table.id == id).all()


    def get_models(self, model: AbstractModel) -> list[AbstractModel]:
        '''
        Получить модели из таблицы данных соответствующей модели
        '''
        return [table.model() for table in self.get(model)]


    def get_one_model(self, model: AbstractModel, id: int) -> AbstractModel:
        '''
        Получить модель из БД
        '''
        return self.get_one(model, id).model()


    def get_ones_models(self, model: AbstractModel, id: int) -> list[AbstractModel]:
        '''
        Получить все модели всех обектов совпадающих с моделью
        '''
        return [table.model() for table in self.get_ones(model, id)]
            
    # TODO: Сделать get с фильтрацией

    # TODO: Сделать add и update с таблицами
    def add(self, model: AbstractModel) -> bool: 
        '''
        Добавление модели в БД
        '''
        table_object = table_factory.create(model)
        # TODO: проверка на корректность объекта и возможность его добавления
        self.session.add(table_object)
        self.session.commit()

        return True


    def update(self, model: AbstractModel) -> bool:
        '''
        Обновление данных соотвутсвующих модели в БД
        '''
        current_table_object = table_factory.create(model)
        was_table_object = self.get_one(model, model.id)
        
        current_vars = set([var for var in vars(current_table_object) if not var.startswith('_')])
        was_vars = set([var for var in vars(was_table_object) if not var.startswith('_')])
        all_vars = current_vars & was_vars

        for var in all_vars:
            if getattr(current_table_object, var) != getattr(was_table_object, var):
                setattr(was_table_object, var, getattr(current_table_object, var))
        
        self.session.commit()

        return True
        

