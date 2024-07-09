from pathlib import Path
from subprocess import run

from .generator import Generator
from .cls import Cls
from .method import Method
from .param import Param

from eazydocs.markdown.writer import Writer
from eazydocs.markdown.updater import Updater


def create_md_file(
    cls_or_method: Cls | Method,
    filename: str = "README",
    filepath: str | Path = None,
) -> Generator:
    cls = Cls(cls_or_method)
    generator = Generator(cls)

    contents = generator.docs.rstrip()

    Writer(contents, filename=filename, filepath=filepath).write()


def update_md_file(
    cls_or_method: Cls | Method,
    filename: str = "README",
    filepath: str | Path = None,
) -> Generator:
    Updater(cls_or_method, filename, filepath)


def get_method_docs(method: object, to_clipboard: bool = False) -> str:
    method = Method(method)
    generator = Generator(method)

    if to_clipboard:
        run(["clip.exe"], input=generator.docs.strip().encode("utf-8"))

    return generator.docs
