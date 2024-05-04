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
        MDFile(filename, docs, filepath)

    return docs


def generate_example(
    code: str,
    df: DataFrame,
    append_to_method: bool = False,
    method_name: None | str = None,
    filename: None | str = None,
    filepath: None | str = None,
) -> str:
    example = Example(code, df).output

    if append_to_method != False:
        if append_to_method and method_name == None:
            raise ValueError("generate_example missing 1 required positional argument: 'method_name'")
        elif append_to_method and filename == None:
            raise ValueError("generate_example missing 1 required positional argument: 'filename'")

        filename = filename.strip()
        if filename[-3:] != ".md":
            filename += ".md"

        if filepath == None:
            dir = Path().cwd()
            file = Path(dir, filename)
        else:
            file = Path(filepath, filename)

        with open(file, "r+") as f:
            contents = f.read()

            if contents.__contains__(method_name) is False:
                raise ValueError(f"Unable to find {method_name} in {filename}. Confirm the spelling is correct, as well as the filepath: {file}")

            method_start = contents.find(f">{method_name}<")
            next_method_start = contents.find("<strong", method_start)

            before_example = contents[0:next_method_start]
            after_example = contents[next_method_start:-1]

            if before_example.__contains__("> Example"):
                to_write = before_example + "\n" + example + "\n" + after_example
            else:
                to_write = before_example + "\n\n> Example\n\n" + example + "\n" + after_example

        with open(file, "w") as f:
            f.write(to_write)

        print(f"Succesfully updated {filename}.")

    return example


from subprocess import run

from generator.method import Method

g = generate_docs(generate_docs)
# print(g)

run(["clip.exe"], input=g.encode("utf-8"))
<strong id='generate-docs'>generate_docs</strong>(<b>obj</b>, <b>append_to_file</b><i>=False</i>, <b>filename</b><i>=_NoDefault.no_default</i>, <b>filepath</b><i>=_NoDefault.no_default</i>)

> Parameters

<ul style='list-style: none'>
    <li>
        <b>obj : <i>object</i></b>
        <ul style='list-style: none'>
            <li>description</li>
        </ul>
    </li>
    <li>
        <b>append_to_file : <i>bool, default False</i></b>
        <ul style='list-style: none'>
            <li>description</li>
        </ul>
    </li>
    <li>
        <b>filename : <i>str, optional</i></b>
        <ul style='list-style: none'>
            <li>description</li>
        </ul>
    </li>
    <li>
        <b>filepath : <i>str, optional</i></b>
        <ul style='list-style: none'>
            <li>description</li>
        </ul>
    </li>
</ul>