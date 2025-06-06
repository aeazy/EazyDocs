from pathlib import Path

from eazydocs.core import Generator
from eazydocs.core.common import check_filename, set_path


class Writer:
    def __init__(
        self,
        contents: str | Generator,
        filename: str,
        filepath: str | Path = None,
    ) -> None:
        self.contents = contents

        filename = check_filename(filename)

        if filepath is not None:
            if isinstance(filepath, str):
                filepath = Path(filepath)
            path = filepath.joinpath(filename)
        else:
            path = Path(filename)

        self.path = path

        if isinstance(contents, Generator):
            contents = contents.docs

    def write(self) -> None:
        try:
            with open(self.path, "w") as f:
                f.write(self.contents)
        except FileNotFoundError:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w") as f:
                f.write(self.contents)