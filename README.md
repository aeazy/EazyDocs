# EazyDocs

EazyDocs provides a simple way to generate documentation for Python classes and
methods. By providing a class or method object, you can generate a markdown (MD)
file that mixes markdown and html formatting to clearly define your code.

### Table of Contents

- [Installation](#installation)
- [Methods](#methods)
  - [`get_documentation`](#get-documentation)
  - [`create_md_file`](#create-md_file)
  - [`update_md_file`](#update-md-file)
  - [`get_example`](#get-example)

## Installation

- Install the eazydocs module using your preferred package manager:z
  ```
  pip install eazydocs
  ```
- Alternatively, the .whl can be downloaded and installed:
  ```
  pip install eazydocs-X.X.X-py3-none-any.whl
  ```

## Methods

<strong id='get-documentation'>get_documentation</strong>(<b>class_or_method</b>=<i>None</i>, <b>include_methods</b>=<i>True</i>, <b>include_private_methods</b>=<i>False</i>, <b>include_examples</b>=<i>True</i>, <b>to_clipboard</b>=<i>True</i>)

Generate documentation for a class or method.

> Parameters:

<ul>
    <li>
        <b id='get_documentation-class_or_method'>class_or_method : <i>object | FunctionType | MethodType, None</i></b>
        <ul style='list-style: none'>
            <li id='get_documentation-class_or_method-description'>The class or method to generate documentation for.</li>
        </ul>
    </li>
    <li>
        <b id='get_documentation-include_methods'>include_methods : <i>bool, optional, True</i></b>
        <ul style='list-style: none'>
            <li id='get_documentation-include_methods-description'>Whether to include methods in the documentation. Defaults to True.</li>
        </ul>
    </li>
    <li>
        <b id='get_documentation-include_private_methods'>include_private_methods : <i>bool, optional, False</i></b>
        <ul style='list-style: none'>
            <li id='get_documentation-include_private_methods-description'>Whether to include private methods in the documentation. Defaults to False.</li>
        </ul>
    </li>
    <li>
        <b id='get_documentation-include_examples'>include_examples : <i>bool, optional, True</i></b>
        <ul style='list-style: none'>
            <li id='get_documentation-include_examples-description'>Whether to include examples in the documentation. Defaults to True.</li>
        </ul>
    </li>
    <li>
        <b id='get_documentation-to_clipboard'>to_clipboard : <i>bool, optional, True</i></b>
        <ul style='list-style: none'>
            <li id='get_documentation-to_clipboard-description'>If True, the output will be copied to the clipboard. Defaults to True.</li>
        </ul>
    </li>
</ul>

> Examples:

Basic Usage with a Class:

```python
from eazydocs import get_documentation

>>> get_documentation(ExampleClass)
Successfully copied to clipboard!
```

- Output for `ExampleClass` will contain the documentation for the class and its
  methods.
- Using `include_methods=False` will exclude methods from the output.
- Using `include_private_methods=True` will include private methods in the
  output.
- Using `include_examples=False` will exclude examples from the output.
- Using `to_clipboard=False` will allow you to print the output to the console
  instead of copying it to the clipboard.

Basic Usage with a Method:

```python
from eazydocs import get_documentation

>>> get_documentation(ExampleClass.example_method)
Successfully copied to clipboard!
```

- Output for `ExampleClass.example_method` will contain the documentation for the
  method only.

<hr>

<strong id='create-md-file'>create_md_file</strong>(<b>class_or_method</b>=<i>None</i>, <b>filename</b>=<i>"README.md"</i>, <b>path</b>=<i>None</i>, <b>overwrite</b>=<i>False</i>)

Generate a markdown file for a class or method.

> Parameters:

<ul>
    <li>
        <b id='create_md_file-class_or_method'>class_or_method : <i>ClassMethodType, None</i></b>
        <ul style='list-style: none'>
            <li id='create_md_file-class_or_method-description'>Class or method to generate documentation for.</li>
        </ul>
    </li>
    <li>
        <b id='create_md_file-filename'>filename : <i>StrPathType, optional, "README.md"</i></b>
        <ul style='list-style: none'>
            <li id='create_md_file-filename-description'>String or Path object for the filename. If a string object is provided, the file will be saved to the current working directory. Defaults to "README.md".</li>
        </ul>
    </li>
    <li>
        <b id='create_md_file-path'>path : <i>StrPathType, optional, None</i></b>
        <ul style='list-style: none'>
            <li id='create_md_file-path-description'>Directory path where the file will be saved. If not provided, the file will be saved in the current working directory. If provided, the <code>filename</code> will be joined to <code>path</code> argument. Defaults to None.</li>
        </ul>
    </li>
    <li>
        <b id='create_md_file-overwrite'>overwrite : <i>bool, optional, False</i></b>
        <ul style='list-style: none'>
            <li id='create_md_file-overwrite-description'>If True, the existing file will be overwritten without confirmation. Defaults to False.</li>
        </ul>
    </li>
</ul>

> Examples:

Basic Usage:

```python
from eazydocs import create_md_file

>>> create_md_file(ExampleClass)
Successfully created markdown file: 'README.md'
```

- File is created in the current working directory with the name "README.md".

Specifying a filename and path:

```python
from eazydocs import create_md_file

>>> create_md_file(ExampleClass, filename="ExampleClass.md", path="./docs")
Successfully created markdown file: './docs/ExampleClass.md'
```

<hr>

<strong id='update-md-file'>update_md_file</strong>(<b>class_or_method</b>=<i>None</i>, <b>filename</b>=<i>None</i>, <b>path</b>=<i>None</i>)

Update an EazyDocs generated markdown file. If a class is provided, it will overwrite the provided file. Otherwise, it will trim the old method documentation from the file, insert the updated documentation, and write it to the given `filename`.

> Parameters:

<ul>
    <li>
        <b id='update_md_file-class_or_method'>class_or_method : <i>ClassMethodType, None</i></b>
        <ul style='list-style: none'>
            <li id='update_md_file-class_or_method-description'>Class or method to update.</li>
        </ul>
    </li>
    <li>
        <b id='update_md_file-filename'>filename : <i>StrPathType, None</i></b>
        <ul style='list-style: none'>
            <li id='update_md_file-filename-description'>String or Path object representing the markdown file to update.</li>
        </ul>
    </li>
    <li>
        <b id='update_md_file-path'>path : <i>StrPathType, optional, None</i></b>
        <ul style='list-style: none'>
            <li id='update_md_file-path-description'>String or Path object for the path where the file will be saved. If not provided, the file will be saved in the current working directory. If provided, the <code>filename</code> will be joined to <code>path</code> argument. Defaults to None.</li>
        </ul>
    </li>
</ul>

> Notes:

- The markdown file must have been generated by EazyDocs for the update to work.
- Updating a class will overwrite the entire file.

> Examples:
> Basic Usage with a Class:

```python
from eazydocs import update_md_file

>>> update_md_file(ExampleClass, filename="README.md")
Successfully updated markdown file: 'README.md'
```

- Since a class is provided, the entire file will be overwritten with the new
  documentation.

Basic Usage with a Method:

```python
from eazydocs import update_md_file

>>> update_md_file(ExampleClass.example_method, filename="README.md")
Successfully updated markdown file: 'README.md'
```

- Since a method is provided, only the documentation for that method will be
  updated in the file.

<hr>

<strong id='get-example'>get_example</strong>(<b>arg</b>=<i>None</i>, <b>df_shape</b>=<i>None</i>, <b>copy_to_clipboard</b>=<i>True</i>, <b>append_to_method</b>=<i>None</i>, <b>filename</b>=<i>None</i>, <b>path</b>=<i>None</i>)

Generate an example representation of a DataFrame or method.

> Parameters:

<ul>
    <li>
        <b id='get_example-arg'>arg : <i>DataFrame | FunctionMethodType, None</i></b>
        <ul style='list-style: none'>
            <li id='get_example-arg-description'>The DataFrame or method to generate an example for.</li>
        </ul>
    </li>
    <li>
        <b id='get_example-df_shape'>df_shape : <i>tuple[int,int] | DfShape, optional, None</i></b>
        <ul style='list-style: none'>
            <li id='get_example-df_shape-description'>A tuple or DfShape specifying the number of rows and columns to display from the DataFrame. If <code>type(arg)==DataFrame</code> and <code>df_shape=None</code>, the default shape of (5,5) will be used. Defaults to None.</li>
        </ul>
    </li>
    <li>
        <b id='get_example-copy_to_clipboard'>copy_to_clipboard : <i>bool, optional, True</i></b>
        <ul style='list-style: none'>
            <li id='get_example-copy_to_clipboard-description'>If True, the output will be copied to the clipboard. Defaults to True.</li>
        </ul>
    </li>
    <li>
        <b id='get_example-append_to_method'>append_to_method : <i>str, optional, None</i></b>
        <ul style='list-style: none'>
            <li id='get_example-append_to_method-description'>If provided, the example will be appended to the specified method in the markdown file. If <code>append_to_method!=None</code>, <code>filename</code> must also be provided. Optionally providing the <code>path</code> argument. Defaults to None.</li>
        </ul>
    </li>
    <li>
        <b id='get_example-filename'>filename : <i>StrPathType, optional, None</i></b>
        <ul style='list-style: none'>
            <li id='get_example-filename-description'>String or Path object for the filename. Defaults to None.</li>
        </ul>
    </li>
    <li>
        <b id='get_example-path'>path : <i>StrPathType, optional, None</i></b>
        <ul style='list-style: none'>
            <li id='get_example-path-description'>Directory path where the file will be located. Defaults to None.</li>
        </ul>
    </li>
</ul>

> Examples:

Basic Usage with a DataFrame:

```python
import pandas as pd
from eazydocs import get_example

>>> df = pd.DataFrame({
...     "A": range(1, 11),
...     "B": range(11, 21),
})
>>> get_example(df, df_shape=(3, 2))
Successfully copied to clipboard!
```

- Output will be a markdown table representation of the DataFrame with 3 rows and
  2 columns:
  ```markdown
  |   A |   B |
  | --: | --: |
  |   1 |  11 |
  |   2 |  12 |
  |   3 |  13 |
  ```

Basic Usage with a Method:

```python
from eazydocs import get_example

>>> def example_method(x):
...     return x * 2
>>> get_example(example_method)
Successfully copied to clipboard!
```

- Output will be a code block boilerplate for the method:
  ```python
  example_method()
  ```

<hr>
