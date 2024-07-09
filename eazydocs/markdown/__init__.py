from pathlib import Path

from .reader import Reader
from .parser import Parser



def read_md_file(filename: str, filepath: str | Path = None) -> str:        
    with Reader(filename, filepath) as f:
        contents = f.contents
    return contents
