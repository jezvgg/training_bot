from DB.Tables import Base, BaseTable
from sqlalchemy.orm import sessionmaker, Session, Query
from sqlalchemy import create_engine, Engine
from DB.table_factory import table_factory
from Src.Models import AbstractModel
from Src.settings import settings
from DB.DBInterface import DBInterface
from functools import singledispatchmethod


class DBHelper(DBInterface):
    '''
    Класс для работы с БД
    '''
    session: Session
    engine: Engine


    def __init__(self, config: settings):
        url = config.db_url
        url = url.format(**config.database_kwargs())
        self.engine = create_engine(url, echo=False)

        Base.metadata.create_all(bind=self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def __get_type(self, model) -> type:
        if isinstance(model, type):
            return model

        return type(model)


    def _get(self, obj: BaseTable | AbstractModel) -> Query[BaseTable]:
        if issubclass(self.__get_type(obj), BaseTable): return self._get_table(obj)
        elif issubclass(self.__get_type(obj), AbstractModel): return self._get_model(obj)
        return None


    def _get_table(self, table: BaseTable) -> Query[BaseTable]:
        return self.session.query(table)


    def _get_model(self, model: AbstractModel) -> Query[BaseTable]:
        return self.session.query(table_factory.get(model))


    def _get_one(self, table: BaseTable | AbstractModel, id: int) -> BaseTable:
        return self._get(table).filter(table.id == id).one()


    def _get_ones(self, table: BaseTable | AbstractModel, id: int) -> list[BaseTable]:
        return self._get(table).filter(table.id == id).all()


    def get(self, model: BaseTable | AbstractModel) -> list[AbstractModel]:
        return [table.model() for table in self._get(model)]


    def get_one(self, model: BaseTable | AbstractModel, id: int) -> AbstractModel:
        return self._get_one(model, id).model()


    def get_ones(self, model: BaseTable | AbstractModel, id: int) -> list[AbstractModel]:
        return [table.model() for table in self._get_ones(model, id)]


    def _add(self, table: BaseTable) -> bool:
        self.session.add(table)
        self.session.commit()

        return True


    def add(self, model: AbstractModel) -> bool: 
        table_object = table_factory.create(model)
        if len(self.get_ones(model, model.id)) > 0:
            return False

        return self._add(table_object)


    def _update(self):
        self.session.commit()


    def update(self, model: AbstractModel) -> bool:
        current_table_object = table_factory.create(model)
        was_table_object = self._get_one(table_factory.get(model), model.id)
        
        current_vars = set([var for var in vars(current_table_object) if not var.startswith('_')])
        was_vars = set([var for var in vars(was_table_object) if not var.startswith('_')])
        all_vars = current_vars & was_vars

        for var in all_vars:
            if getattr(current_table_object, var) != getattr(was_table_object, var):
                setattr(was_table_object, var, getattr(current_table_object, var))

        self.session.commit()

        return True


    def _delete(self, table: BaseTable) -> bool:
        self.session.delete(table)
        self.session.commit()


    def delete(self, model: AbstractModel) -> bool:
        self._delete(table_factory.create(model))
        

