from os import mkdir
from pathlib import Path
from types import FunctionType, MethodType
from typing import Optional
from eazydocs.core._types import ClassMethodType, StrPathType
from eazydocs.core.method import Method
from eazydocs.core.class_type import ClassType


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


def _get_filepath(
    filename: StrPathType, path: Optional[StrPathType] = None
) -> Path:
    """Get the filepath for the markdown file.


    Args:
        filename (StrPathType): String or Path object for the filename.
        path (StrPathType, optional): Directory path where the file will be
            saved. If not provided, the file will be saved in the current
            working directory. If provided, the `filename` will be joined to
            `path` argument. Defaults to None.

    Returns:
        Path: The Path object representing the filepath for the markdown file.
    """
    if isinstance(filename, str) and not filename.endswith(".md"):
        filename = f"{filename}.md"

    if path is not None:
        if isinstance(path, str):
            path = Path(path)
        filepath = Path(path) / filename
    else:
        if isinstance(filename, str):
            filepath = Path(filename)
        else:
            # Filename is already a Path object - Sanitize it
            if not filename.suffix:
                filename = f"{filename}.md"
            filepath = filename

    if not filepath.exists():
        filepath.parent.mkdir(parents=True, exist_ok=True)
    else:
        while True:
            confirm = input(
                f"Filepath '{filepath}' already exists. Do you want to overwrite it? (y/n): "
            )
            match confirm.lower():
                case "y":
                    print(f"Overwriting existing file: '{filepath}'")
                    break
                case "n":
                    print("Exiting without overwriting the file.")
                    return False
                case _:
                    print("Invalid input. Please enter 'y' or 'n'.")

    return filepath


def create_md_file(
    class_or_method: ClassMethodType,
    filename: StrPathType = "README.md",
    path: Optional[StrPathType] = None,
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
    """
    # Get the filepath
    filepath = _get_filepath(filename, path)
    if not filepath:
        return
    # Generate the documentation
    docs = get_documentation(class_or_method, to_clipboard=False)

    with open(filepath, "w+") as f:
        f.write(docs)

    print(f"Successfully created markdown file: '{filepath}'")
