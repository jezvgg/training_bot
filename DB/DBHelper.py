from DB.Tables import Base, BaseTable
from sqlalchemy.orm import sessionmaker, Session, Query
from sqlalchemy import create_engine, Engine
from DB.table_factory import table_factory
from Src.Models import AbstractModel
from Src.settings import settings
from DB.DBInterface import DBInterface


class DBHelper(DBInterface):
    '''
    Класс для работы с БД
    '''
    session: Session
    engine: Engine


    def __init__(self, config: settings):
        url = "postgresql://{user}:{password}@{host}:{port}/{database}".format(**config.database_kwargs())
        self.engine = create_engine(url, echo=False)

        Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def _get(self, model: AbstractModel) -> Query[BaseTable]:
        return self.session.query(table_factory.get(model))


    def _get_one(self, model: AbstractModel, id: int) -> BaseTable:
        table = table_factory.get(model)
        return self.session.query(table).filter(table.id == id).one()


    def _get_ones(self, model: AbstractModel, id: int) -> list[BaseTable]:
        table = table_factory.get(model)
        return self.session.query(table).filter(table.id == id).all()


    def get(self, model: AbstractModel) -> list[AbstractModel]:
        return [table.model() for table in self._get(model)]


    def get_one(self, model: AbstractModel, id: int) -> AbstractModel:
        return self._get_one(model, id).model()


    def get_ones(self, model: AbstractModel, id: int) -> list[AbstractModel]:
        return [table.model() for table in self._get_ones(model, id)]


    def _add(self, table: BaseTable) -> bool:
        self.session.add(table)
        self.session.commit()

        return True


    def add(self, model: AbstractModel) -> bool: 
        table_object = table_factory.create(model)
        if self.get_one(model, model.id) is not None:
            return False

        return self._add(table_object)


    def update(self, model: AbstractModel) -> bool:
        current_table_object = table_factory.create(model)
        was_table_object = self._get_one(model, model.id)
        
        current_vars = set([var for var in vars(current_table_object) if not var.startswith('_')])
        was_vars = set([var for var in vars(was_table_object) if not var.startswith('_')])
        all_vars = current_vars & was_vars

        for var in all_vars:
            if getattr(current_table_object, var) != getattr(was_table_object, var):
                setattr(was_table_object, var, getattr(current_table_object, var))

        self.session.commit()

        return True
        

