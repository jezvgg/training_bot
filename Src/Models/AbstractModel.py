from abc import ABC, abstractclassmethod


class AbstractModel(ABC):

    def __repr__(self):
        classname = str(self.__class__)
        fields = [f"{str(field)}={str(getattr(self, field))}" for field in dir(self) if not field.startswith('_')]
        return f"{classname}({', '.join(fields)})"


    @property
    def id(self):
        return None