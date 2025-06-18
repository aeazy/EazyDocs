from types import FunctionType, MethodType
from typing import Optional
from eazydocs.core._types import ClassMethodType, StrPathType
from eazydocs.core.method import Method
from eazydocs.core.class_type import ClassType
from eazydocs.markdown.writer import Writer


def get_documentation(
    class_or_method: ClassMethodType,
    include_methods: bool = True,
    include_private_methods: bool = False,
    include_examples: bool = True,
    to_clipboard: bool = True,
) -> str:
    """Generate documentation for a class or method.

    Args:
        class_or_method (object | FunctionType | MethodType): The class or
            method to generate documentation for.
        include_methods (bool, optional): Whether to include methods in the
            documentation. Defaults to True.
        include_private_methods (bool, optional): Whether to include private
            methods in the documentation. Defaults to False.
        include_examples (bool, optional): Whether to include examples in the
            documentation. Defaults to True.
        to_clipboard (bool, optional): If True, the output will be copied to the
            clipboard. Defaults to True.
    """
    if isinstance(class_or_method, (FunctionType, MethodType)):
        method = Method(class_or_method, include_examples=include_examples)
        docs = method.parse(to_clipboard=to_clipboard)
    else:
        cls = ClassType(
            class_or_method,
            include_methods=include_methods,
            include_private_methods=include_private_methods,
            include_examples=include_examples,
        )
        docs = cls.parse(to_clipboard=to_clipboard)

    return docs


def create_md_file(
    class_or_method: ClassMethodType,
    filename: StrPathType = "README.md",
    path: Optional[StrPathType] = None,
    overwrite: bool = False,
    **kwargs,
) -> None:
    """Generate a markdown file for a class or method.

    Args:
        class_or_method (ClassMethodType): Class or method to generate
            documentation for.
        filename (StrPathType, optional): String or Path object for the
            filename. If a string object is provided, the file will be saved to
            the current working directory. Defaults to "README.md".
        path (StrPathType, optional): Directory path where the file will be
            saved. If not provided, the file will be saved in the current
            working directory. If provided, the `filename` will be joined to
            `path` argument. Defaults to None.
        overwrite (bool, optional): If True, the existing file will be
            overwritten without confirmation. Defaults to False.
    """
    docs = get_documentation(class_or_method, to_clipboard=False)

    writer = Writer(
        contents=docs,
        filename=filename,
        path=path,
        overwrite=overwrite,
        **kwargs,
    )

    writer.write()


def update_md_file(
    class_or_method: ClassMethodType,
    filename: StrPathType,
    path: Optional[StrPathType] = None,
) -> None:
    """Update an EazyDocs generated markdown file.

    If a class is provided, it will overwrite the provided file. Otherwise, it
    will trim the old method documentation from the file, insert the updated
    documentation, and write it to the given `filename`.

    Args:
        class_or_method (ClassMethodType): Class or method to update.
        filename (StrPathType): String or Path object representing the
            markdown file to update.
        path (StrPathType, optional): String or Path object for the path
            where the file will be saved. If not provided, the file will be
            saved in the current working directory. If provided, the
            `filename` will be joined to `path` argument. Defaults to None.
    """
    from eazydocs.markdown.updater import Updater

    Updater(class_or_method, filename, path)
