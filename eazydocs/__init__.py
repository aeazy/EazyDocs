from pandas import DataFrame

from method.method import Method
from example.example import Example
from markdown.markdown import Markdown


def generate_docs(
    method_name: str,
    method_parameters: list[str],
    df_example: tuple[str, DataFrame] = None,
    append_to_file: bool = False,
    filename: None | str = None,
    filepath: None | str = None,
):
    docs = Method(method_name, method_parameters).output

    if df_example != None:
        example = Example(df_example[0], df_example[1]).output
        docs += f"\n\n> Example\n\n{example}"

    if append_to_file == False:
        return docs
    else:
        Markdown(filename, docs, filepath)
