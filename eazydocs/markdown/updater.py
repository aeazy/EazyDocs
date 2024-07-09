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
            raise NotImplementedError(
                "Use the create_md_file method to update docs for an entire class"
            )
            self.arg = Cls(cls_or_method)
            self.update_file()
        elif isfunction(cls_or_method) or ismethod(cls_or_method):
            self.arg = Method(cls_or_method)
            self._update_method()

    def update_file(self) -> None:
        for method in self.arg.methods:
            start, end = self._find_method_docs(method.name)
            print(start, end)
        # for each method - find <strong
        # then find next method

    def _update_method(self) -> None:
        generator = Generator(self.arg)
        docs = generator.docs

        if self._is_new_method(self.arg.name):
            new_docs = f"{self.current_docs}\n{docs}"
            self._create_markdown(new_docs)
        else:
            self._trim_old_method(self.arg.name, docs)

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

    def _trim_old_method(self, method: str, method_docs: str) -> str:
        start, end = self._find_method_docs(method)
        before, after = self._get_before_after_docs(start, end)
        new_docs = f"{before}\n\n{method_docs}\n{after}"

        self._create_markdown(new_docs)

    def _find_method_docs(self, method: str) -> tuple[int, int]:
        start = self.current_docs.find(method) - (len(method) + 14)
        end = self.current_docs[start:].find("<hr>") + 4

        return (start, end)

    def _get_before_after_docs(self, start: int, end: int) -> tuple[str, str]:
        before = self.current_docs[:start].strip()
        after = self.current_docs[(start + end) :].strip()

        return (before, after)
