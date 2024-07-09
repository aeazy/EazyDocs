from inspect import isclass, ismethod, isfunction
from pathlib import Path

from eazydocs.core.common import check_filename, set_path
from eazydocs.core import Cls, Generator, Method, Param

from .reader import Reader
from .md_method import MDMethod


class Updater:
    def __init__(
        self,
        cls_or_method: object,
        filename: str,
        filepath: str | Path = None,
    ) -> None:
        if isclass(cls_or_method):
            self.arg = Cls(cls_or_method)
        elif isfunction(cls_or_method) or ismethod(cls_or_method):
            self.arg = Method(cls_or_method)
        filename = check_filename(filename)

        if filepath is not None:
            filename = set_path(filename, filepath)

        self.filename = filename

        self.update()

    def update(self) -> None:
        with Reader(self.filename) as f:
            contents = f.contents

        self._get_current_methods(contents)

        if isinstance(self.arg, Cls):
            self._get_description(self.arg.name, self.arg.params)
            # cls_params = self.arg.params
            # for param in cls_params:
            #     print(param.name)
            # for method in self.arg.methods:
            #     print(method.name)

    # def _get_description(self, name: str, params: list[Param]) -> str:
    #     records: dict = self.current_methods.get(name)[name]

    #     params = [param.name for param in params]

    #     # for param in params:
    #     #     current_description: str = records.get(param)["description"]
    #     #     if description == "_description_":
    #     for param in self.arg.params:
    #         if param.description == "_description_":
    #             current_description = records.get(param.name)
    #             print(current_description)
    #         # if p.name == param:
    #         #     p.description = "new description"

    #     g = Generator(self.arg)
    #     # print(g.docs)

    # def _get_current_methods(self, docs: str) -> None:
    #     methods: dict[str:MDMethod] = dict()

    #     docs = docs.split("<strong")
    #     for doc in docs:
    #         if doc.lstrip().startswith("id"):
    #             method = MDMethod(doc)
    #             methods.update({method.name: method.params})

    #     self.current_methods = methods

    #     # for doc in methods:
    #     #     method = self._convert_method(doc)

    # def _convert_method(self, arg: MDMethod) -> Method:
    #     method = Method()
    #     method.name = arg.name

    #     for key, params in arg.params.items():
    #         for item in params.items():
    #             param = Param(item)
    #             method.params.append(param)

    #     return method
