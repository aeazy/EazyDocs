# EazyDocs

eazydocs looks to provide an easy way to generate code documentation by cutting down repetitive boilerplate input. With as little as the function name and its parameters, you can generate a markdown file that mixes markdown and html formatting to clearly define your code.

## Getting started

- Install the eazydocs module using your preferred package manager:z
  ```
  pip install eazydocs
  ```
- Alternatively, the .whl can be downloaded and installed:
  ```
  pip install eazydocs-24.X.X-py3-none-any.whl
  ```

eazydocs.generate_docs()

## Usage
```
from eazydocs import generate_docs




Args:
name (str): String representation of the method name.
params (list[str]): List of strings where the string expression follows a specific formatting. See below to understand syntax, as well as the special characters that allow you to easily mix in html formatting.

Parameter Syntax:
The order of the variables in the string expression is as follows: parameter_name : parameter_type : default argument / parameter_description. ':' specifies the end of a parameter variable. '/' specifies the start of the parameter description.

Special Characters:
':' - Specifies the end of a parameter.
'/' - Specifies the start of the function description.
'{' - Specifies the start of a codeblock.
'}' - Specifies the end of a codeblock.

Example: >>> def example_function(s1: str, s2: str = 'Example'):
...

    >>> Method('example_function', ["s1:str:/String expression of word to join to s2.", "s2:str:'Example'/String expression of word to join s1 to."])

    <strong id='example-function'>example_function</strong>(<b>s1</b>, <b>s2</b><i>='Example'</i>)

    > Parameters

    <ul style='list-style: none'>
        <li>
            <b>s1 : <i>str</i></b>
            <ul style='list-style: none'>
                <li>String expression of word to join to s2.</li>
            </ul>
        </li>
        <li>
            <b>s2 : <i>str, default 'Example'</i></b>
            <ul style='list-style: none'>
                <li>String expression of word to join s1 to.</li>
            </ul>
        </li>
    </ul>

"""
