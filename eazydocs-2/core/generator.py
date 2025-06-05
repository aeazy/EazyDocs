from types import FunctionType
from typing import Optional

from eazydocs.core import ClassType, MethodType


class Generator:
    def __init__(
        self,
        class_or_method: object | FunctionType,
        include_methods: Optional[bool] = True,
        include_private_methods: Optional[bool] = False,
        include_examples: Optional[bool] = True,
    ):

        if isinstance(class_or_method, FunctionType):
            # Pass to Method class to parse and return docstring
            parser = MethodType(
                class_or_method,
                include_examples=include_examples,
            )
        elif isinstance(class_or_method, type):
            # Assume class is passed
            parser = ClassType(
                class_or_method,
                include_methods=include_methods,
                include_private_methods=include_private_methods,
                include_examples=include_examples,
            )

        self.output = parser.format_docs()

    def __repr__(self):
        return self.output

    def create_md_file(self, filename="README.md"):
        if not filename.endswith(".md"):
            filename = f"{filename}.md"

        with open(filename, "w") as f:
            f.write(self.output)

        return f"Successfully created {filename}"


def generate_md_file(
    class_or_method: object | FunctionType,
    filename: str = "README.md",
    include_methods: Optional[bool] = True,
    include_private_methods: Optional[bool] = False,
    include_examples: Optional[bool] = True,
) -> None:
    """Generate a markdown file for a class or method.

    Args:
        class_or_method (object | FunctionType): Class or method to generate
            documentation for. If a class is passed, all methods will be
            included in the documentation.
        filename (str, optional): Filename to save the markdown file. Defaults
            to "README.md".
        include_methods (Optional[bool], optional): Whether or not methods are
            included if `class_or_method` argument is a class type. Defaults to
            True.
        include_private_methods (Optional[bool], optional): Whether or not
            private methods are included if `class_or_method` argument is a
            class type. Defaults to True. Defaults to False.
        include_examples (Optional[bool], optional): Include examples if found
            in the method docstring. Defaults to True.
    """

    generator = Generator(
        class_or_method=class_or_method,
        include_methods=include_methods,
        include_private_methods=include_private_methods,
        include_examples=include_examples,
    )

    generator.create_md_file(filename=filename)
