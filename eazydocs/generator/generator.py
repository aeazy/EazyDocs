from inspect import getmembers, signature, isfunction, ismethod

from generator.parameters import Parameters


class Generator:
    def __init__(self, cls: object) -> None:
        self.name = cls.__name__
        self.docs = str()

        self.generate_docs(cls)

    def generate_docs(self, cls: object) -> None:
        for name, member in getmembers(cls):
            if name[0:2] == "__" and name != "__init__":
                pass
            elif ismethod(member) or isfunction(member):
                if self.__check_params__(member):
                    params = Parameters(member).params
                    self.docs += f"\n{params}\n"

        self.__fmt_class_name__()

    def __repr__(self) -> str:
        return self.docs

    def __check_params__(self, method) -> bool:
        params = signature(method).parameters
        params = [param for param in params.keys() if param != "self"]
        if params == []:
            return False

        return True

    def __fmt_class_name__(self) -> None:
        if self.docs.__contains__("__init__"):
            docs = self.docs.replace("--init--", self.name.lower())
            docs = docs.replace("__init__", self.name)
            self.docs = docs
