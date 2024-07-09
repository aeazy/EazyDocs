from inspect import isclass, ismethod, isfunction
from pathlib import Path

from eazydocs.core.common import check_filename, set_path
from eazydocs.core import Cls, Generator, Method, Param

from .reader import Reader
from .parser import Parser
from .writer import Writer


class Updater:
    def __init__(
        self,
        cls_or_method: object,
        filename: str,
        filepath: str | Path = None,
    ) -> None:
        filename = check_filename(filename)

        if filepath is not None:
            filename = set_path(filename, filepath)

        self.filename = filename

        self._get_current_docs()

        if isclass(cls_or_method):
            self.arg = Cls(cls_or_method)
            self.update_file()
        elif isfunction(cls_or_method) or ismethod(cls_or_method):
            self.arg = Method(cls_or_method)
            self._update_method()

    def update_file(self) -> None:
        pass

    def _update_method(self) -> None:
        if self._is_new_method(self.arg.name):
            generator = Generator(self.arg)
            docs = generator.docs
            new_docs = f"{self.current_docs}\n{docs}"
            self._create_markdown(new_docs)

        for param in self.arg.params:
            print(param.name)

    def _get_current_docs(self) -> None:
        with Reader(self.filename) as f:
            self.current_docs = f.contents

        parser = Parser(self.current_docs)
        self.current_methods = parser.methods

    def _is_new_method(self, method: str) -> bool:
        if self.current_methods.get(method) is None:
            return True
        return False

    def _create_markdown(self, contents: str) -> None:
        writer = Writer(contents, self.filename)
        writer.write()