from types import FunctionType
from typing import Optional

from ._parser import Parser


class MethodType(Parser):
    def __init__(
        self,
        method: FunctionType,
        include_examples: Optional[bool] = True,
    ):
        super().__init__(method)
        self.run()

        self.method = method
        self.include_examples = include_examples

        self.output = None

    def __repr__(self):
        if self.output is None:
            self.output = self.format_docs()

        return self.output

    def format_docs(self) -> str:
        docs = f"{self.function}\n\n"

        if self.summary:
            docs += f"{self.summary}\n\n"
        if self.args:
            docs += f"> Parameters:\n\n{self.args}\n"
        if self.examples and self.include_examples:
            docs += f"> Examples:\n{self.examples}\n"

        docs += "\n<hr>\n"

        return docs
