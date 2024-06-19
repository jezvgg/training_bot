from DB.Tables import Base
from typing import Callable


class BaseTable(Base):
    __abstract__ = True
    id: int


    @classmethod
    def build(cls, model):
        '''
        Фабричный метод создания таблицы из модели
        '''
        # Получаем публичные поля и property
        class_vars = set([var for var in dir(cls) if not var.startswith('_') and not isinstance(getattr(cls, var), Callable)])
        model_vars = set([var for var in dir(model) if not var.startswith('_') and not isinstance(getattr(model, var), Callable)])
        # Поля находящиеся и там и там
        args = class_vars & model_vars
        kwargs = {}
        for arg in args:
            kwargs[arg] = getattr(model, arg)
        
        return cls(**kwargs)


    def __repr__(self):
        classname = str(self.__class__.__name__)
        fields = [f"{str(field)}={str(getattr(self, field))}" for field in vars(self) if not field.startswith('_')]
        return f"{classname}({', '.join(fields)})"


    def _convert(self, model, **kwargs):
        '''
        Конвертация объекта в модель класса model
        '''
        # Получаем публичные поля и property
        class_vars = set([var for var in dir(model) if not var.startswith('_') and not isinstance(getattr(model, var), Callable)])
        model_vars = set([var for var in dir(self) if not var.startswith('_') and not isinstance(getattr(self, var), Callable)])
        # Поля находящиеся и там и там
        args = class_vars & model_vars
        kwarg = {}
        for arg in args:
            value = getattr(self, arg)

            if value is None and arg in kwargs.keys(): 
                kwarg[arg] = kwargs[arg]

            kwarg[arg] = value
        
        return model(**kwarg)


    def model(self):
        '''
        Фабричный метод возращающий модель с данными из таблицы
        '''
        pass
