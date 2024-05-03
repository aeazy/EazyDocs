"""eazydocs.method mixes markdown and html formatting to format function parameters for your README files.

Args:
    name (str): String representation of the method name.
    params (list[str]): List of strings where the string expression follows a specific formatting. See below to understand syntax, as well as the special characters that allow you to easily mix in html formatting.

Parameter Syntax:
    The order of the variables in the string expression is as follows: parameter_name : parameter_type : default argument / parameter_description. ':'  specifies the end of a parameter variable. '/' specifies the start of the parameter description.

Special Characters:
    ':' - Specifies the end of a parameter.
    '/' - Specifies the start of the function description.
    '{' - Specifies the start of a codeblock.
    '}' - Specifies the end of a codeblock.

Example:
    >>> def example_function(s1: str, s2: str = 'Example'):
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

from dataclasses import dataclass

from method.templates import DEFAULT_ARG_TEMPLATE, TEMPLATE


@dataclass
class Param:
    name: str
    arg_type: str
    default_arg: str
    description: str


class Method:
    def __init__(self, name: str, params: list[str]) -> None:
        self.fn = self.__generate_fn__(name)

        self.name = name
        self.params = params

        self.get_output()

    def get_output(self) -> None:
        params = self.__fmt_params__()
        fn = self.fn.removesuffix(", ") + ")"

        self.output = f"{fn}\n{params}</ul>"

    def __repr__(self) -> str:
        return self.output

    def __fmt_params__(self) -> str:
        blockquote = "> Parameters"
        output = f"\n{blockquote}\n\n<ul style='list-style: none'>\n"

        for param in self.params:
            parsed_param = self.__parse_arg__(param)
            self.__append_param__(parsed_param)
            output += self.__fmt_arg__(parsed_param)

        return output

    def __parse_arg__(self, param: str) -> Param:
        param = param.split("/")

        variables = param[0].split(":")
        variables = [var.strip() for var in variables]

        if len(variables) < 2:
            raise ValueError("Parameter name and type is required.")

        name = variables[0]
        arg_type = variables[1]

        try:
            default_arg = variables[2]
        except IndexError:
            default_arg = ""

        description = param[-1]
        description = description.replace("{", "<code>").replace("}", "</code>").strip()

        return Param(name, arg_type, default_arg, description)

    def __fmt_arg__(self, param: Param) -> str:
        if param.default_arg != "":
            param_template = DEFAULT_ARG_TEMPLATE
        else:
            param_template = TEMPLATE

        param_template = (
            param_template.replace("{name}", param.name)
            .replace("{type}", param.arg_type)
            .replace("{default_arg}", param.default_arg)
            .replace("{description}", param.description)
        )

        return param_template

    def __generate_fn__(self, arg: str) -> str:
        arg = arg.strip()
        arg_id = arg.replace("_", "-")
        return f"<strong id='{arg_id}'>{arg}</strong>("

    def __append_param__(self, param: Param) -> None:
        name = param.name
        default_arg = param.default_arg

        to_append = f"<b>{name}</b>"

        if default_arg != "":
            to_append += f"<i>={default_arg}</i>, "
        else:
            to_append += ", "

        self.fn += to_append
