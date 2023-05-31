from typing import TypeVar, Dict, Any

TModel = TypeVar("TModel")


class BaseModel:
    @classmethod
    def create_model(cls, data: Dict[str, Any]) -> TModel:
        instance = cls()
        for attr_name in cls.__annotations__.keys():
            if data.get(attr_name):
                cls.__setattr__(instance, attr_name, data[attr_name])
        return instance

    def __eq__(self, other: TModel):
        return self.id == other.id

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self}>"

    def __str__(self):
        return self.name
