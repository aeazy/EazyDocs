from pathlib import Path
from typing import Literal


class Markdown:
    def __init__(
        self,
        filename: str,
        filepath: str | Path = None,
    ) -> None:
        if filepath is not None:
            if isinstance(filepath, str):
                filepath = Path(filepath)

            self.filepath = filepath
            self.filename = filepath.joinpath(filename)
        else:
            self.filename = filename

    # Context Manager Interface
    def __enter__(self):
        self.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> Literal[False]:
        return False

    def load(self, filename: str = None) -> None:
        if self.filename is None:
            raise TypeError("Invalid argument provided for 'filename'")
        elif filename is not None:
            self.filename = filename

        self._check_filename()

        with open(self.filename, "r") as f:
            self.contents = f.read()

    def _check_filename(self) -> None:
        if isinstance(self.filename, Path):
            file = self.filename.parts[-1]
        elif self.filename is not None:
            file = self.filename

        if not file.endswith(".md"):
            if not self._check_filetype(file):
                raise ValueError(
                    "Invalid file type provided for 'filename' - MDUpdater only supports MD files"
                )
            else:
                file = file.strip() + ".md"

        filepath = Path(self.filepath, file)
        if filepath.exists():
            self.filename = filepath
        else:
            raise FileNotFoundError(f"No such file or directory: {filepath}")

    def _check_filetype(self, filename: str) -> bool:
        if "." in filename:
            parts = filename.split(".")

            ext = parts[-1]  # assume last . is the file extension

            if "md" not in ext:
                return False

        return True
