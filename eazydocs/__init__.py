from inspect import isclass, ismethod, isfunction
from pandas import DataFrame
from pathlib import Path

from generator.example import Example
from generator.generator import Generator
from generator.parameters import Parameters

from md.md_file import MDFile


def generate_docs(obj: object, append_to_file: bool = False, filename: str = None, filepath: str = None) -> str:
    if isclass(obj):
        docs = Generator(obj).docs
    elif isfunction(obj) or ismethod(obj):
        docs = Parameters(obj).params

    docs = docs.strip()

    if append_to_file != False:
        MDFile(filename, docs, filepath).append()

    return docs


def generate_example(
    df: DataFrame,
    df_shape: list[int] = [5, 5],
    code: str = "df",
    append_to_file: bool = False,
    filename: str = None,
    filepath: str = None,
    method_name: str = None,
) -> str:
    example = Example(code, df, df_shape).output

    # if append_to_file != False:
    #     if append_to_file and method_name == None:
    #         raise ValueError("generate_example missing 1 required positional argument: 'method_name'")
    #     elif append_to_file and filename == None:
    #         raise ValueError("generate_example missing 1 required positional argument: 'filename'")

    if append_to_file != False:
        if filename == None:
            raise ValueError(
                "generate_example missing 1 required positional argument: 'filename'. Set 'append_to_file=False', if you would like the string output of this function."
            )
        
        if method_name != None:
            MDFile(filename, example, filepath).append_to_param(method_name)
        else:
            MDFile(filename, example, filepath)




        # with open(file, "w") as f:
        #     f.write(to_write)

        # print(f"Succesfully updated {filename}.")

    return example


from subprocess import run

from generator.method import Method

g = generate_example(DataFrame({'col1':[i for i in range(0,10)]}), append_to_file=True, filename='readme2', method_name='generate_example')
# print(g)

# run(["clip.exe"], input=g.encode("utf-8"))
