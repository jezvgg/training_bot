from abc import ABC


class AbstractModel(ABC):

    def __repr__(self):
        classname = str(self.__class__.__name__)
        fields = []
        for field in dir(self):
            if not field.startswith('_') and type(getattr(type(self), field)) == property and getattr(self, field) is not None:
                fields.append(f"{str(field)}={str(getattr(self, field))}")
        return f"{classname}({', '.join(fields)})"


    @property
    def id(self):
        return None