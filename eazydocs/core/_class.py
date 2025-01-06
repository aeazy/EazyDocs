from inspect import getmembers, isfunction, ismethod
from types import FunctionType
from typing import Optional

from ._method import MethodType
from ._parser import parse

"""Example output:

## ClassType

{function signature}

{summary}

> Parameters:

{...args}

### Class Methods

{Table of Contents}

{...methods}
"""


class ClassType:
    def __init__(
        self,
        cls: object,
        include_table_of_contents: Optional[bool] = True,
        include_methods: Optional[bool] = True,
        include_private_methods: Optional[bool] = False,
        include_examples: Optional[bool] = True,
    ):
        self.name: str = cls.__name__
        self.id = self.name.replace("_", "-")
        self.summary = None
        self.methods: list[MethodType] = list()
        self.table_of_contents = list()

        # Get the docstring of the class
        docstring = cls.__doc__
        if docstring is None:
            docstring = cls.__init__.__doc__

        self.docstring = docstring
        self.include_table_of_contents = include_table_of_contents

        for name, member in getmembers(cls):
            if ismethod(member) or isfunction(member):
                if name == "__init__":
                    self._parse_class_docstring(member)
                elif include_methods:
                    if include_private_methods:
                        self.methods.append(
                            MethodType(
                                member,
                                include_examples=include_examples,
                            )
                        )
                    elif not name.startswith("_"):
                        self.methods.append(
                            MethodType(
                                member,
                                include_examples=include_examples,
                            )
                        )

    def __repr__(self):
        return f"""ClassType(
        name={self.name}, 
        function={self.function},
        id={self.id}, 
        summary={self.summary},
    )"""

    def format_docs(self) -> str:
        docs = f"## {self.name}\n\n"

        docs += f"{self.function}\n\n{self.summary}\n\n"

        if self.args:
            docs += f"> Parameters:\n\n{self.args}\n"

        if self.methods != []:
            docs += "### Class Methods\n\n"
            if self.include_table_of_contents:
                docs += self._build_table_of_contents()
                docs += "\n"

            docs += "\n".join(
                [method.format_docs() for method in self.methods]
            )

        return docs

    def _parse_class_docstring(self, method: FunctionType) -> str:
        """Parse the docstring of the class and extract the summary,
        arguments, and examples.
        """

        function, self.summary, self.args, self.examples = parse(method)

        self.function = self._format_function(function)
        return self.format_docs()

    def _format_function(self, function: str) -> str:
        return function.replace("--init--", self.name).replace(
            "__init__", self.name
        )

    def _build_table_of_contents(self) -> str:
        """Build a table of contents for the class methods."""

        table_of_contents = ""

        for method in self.methods:
            table_of_contents += f"- [{method.name}](#{method.id})\n"

        return table_of_contents
