from inspect import signature
from re import match,findall
from types import FunctionType

from .param import Param


class Method:
    def __init__(self, method: FunctionType = None) -> None:
        self.params: list[Param] = []
        if method is not None:
            self.method = method

            self.docstring = method.__doc__

            self.name = method.__name__
            self.id = self.name.replace("_", "-")

            self.output = None

            if self.docstring is None:
                self._from_signature()
            else:
                self._from_docstring()

    def _from_docstring(self) -> None:
        args_start = self.docstring.find("Args:")
        args = self.docstring[args_start:].replace("Args:", "").strip()
        args = args.split("\n")

        # for arg in args:
        # arg = arg.strip()
        param = findall(r"(\b\w+) \((.+)\): (.+)", args)

        if param is not None:
            print(param.groups())
            
            self.params.append(Param(param))

    def _from_signature(self) -> None:
        params = signature(self.method).parameters

        for key, val in params.items():
            if key != "self":
                self.params.append(Param(val))

    def __repr__(self) -> str:
        return f"name:{self.name}\nparams: {self.params}"
