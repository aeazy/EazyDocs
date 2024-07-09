from inspect import getmembers, isfunction, ismethod

from eazydocs.core.method import Method


class Cls:
    def __init__(self, cls: object) -> None:
        self.name: str = cls.__name__
        self.methods = list()
        self.id = self.name.replace("_", "-")

        for name, member in getmembers(cls):
            if ismethod(member) or isfunction(member):
                if name == "__init__":
                    method = Method(member)
                    self.params = method.params
                elif not name.startswith('_'):
                    self.methods.append(Method(member))
    
    def __repr__(self) -> str:
        return f"name:{self.name}\nmethods:{self.methods}\n"