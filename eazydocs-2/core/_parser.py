import re
from collections import defaultdict
from types import FunctionType

_arg_template = """    <li>
        <b>{name} : <i>{arg_type}, {default_arg}</i></b>
        <ul style='list-style: none'>
            <li>{description}</li>
        </ul>
    </li>
"""

_arg_template_no_default = """    <li>
        <b>{name} : <i>{arg_type}</i></b>
        <ul style='list-style: none'>
            <li>{description}</li>
        </ul>
    </li>
"""


_example_template = """
```python
{example}
```"""


class Parser:
    @property
    def args(self) -> str:
        return self._args

    @args.setter
    def args(self, value: str):
        self._args = value

    @property
    def examples(self) -> str:
        return self._examples

    @examples.setter
    def examples(self, value: str):
        self._examples = value

    @property
    def function(self) -> str:
        return self._function

    @function.setter
    def function(self, value: str):
        self._function = value

    @property
    def id(self) -> str:
        """Uses the name of the method to generate a unique ID for the method."""

        id = self.name.replace("_", "-")
        return id

    @property
    def link(self) -> str:
        return f"[{self.name}](#{self.id})"

    @property
    def summary(self) -> str:
        return self.get_summary()

    def __init__(self, method: object | FunctionType):
        self.name = method.__name__
        self.docstring = method.__doc__
        self.docstring_split = (
            method.__doc__.split("\n") if method.__doc__ else None
        )
        self.params = defaultdict(dict)

        self.args = None
        self.function = None
        self.examples = None

    def run(self) -> str:
        """Run the parser to parse the docstring of the method."""

        self.get_summary()
        self.get_args()
        self.get_examples()
        self.get_function()

    def get_function(self) -> str:
        """Return the function signature of the method."""

        output = f"<strong id='{self.id}'>{self.name}</strong>("

        if self.params == {}:
            output += ")"

        # Add the parameters to the output string with their default values if
        # they exist
        for param in self.params:
            default_value = self.params[param]["default_value"]

            if default_value is None:
                output += f"<b>{param}</b>, "
            elif default_value == "None":
                output += f"<b>{param}</b>=<i>None</i>, "
            else:
                output += f"<b>{param}</b>=<i>{self.params[param]['default_value']}</i>, "

        # Strip the trailing comma and space then add a closing parenthesis
        if output.endswith(", "):
            output = output[:-2] + ")"

        self.function = output

        return self.function

    def get_summary(self) -> str:
        """Parse the docstring and return the summary of the method."""

        if self.docstring_split is None:
            return "No summary found"

        output = ""

        for line in self.docstring_split:
            if line.strip() in ["Args:", "Example:", "Equation:"]:
                break
            else:
                line = line.strip() + " "
                output += line

        output = output.strip()

        return output

    def get_args(self) -> str:
        if self.docstring is None:
            return "No arguments found"

        args_section = re.search(
            r"Args:\n(.*?)(\n\n|\Z)", self.docstring, re.DOTALL
        )

        if not args_section:
            return None

        args_section = args_section.group(1)
        args_pattern = re.compile(
            r"\s*(\w+)\s*\(([\w\s,[\]\|]+)\):\s*(.*?)(?=\n\s*\w+\s*\(|\n\n|\Z)",
            re.DOTALL,
        )
        args = args_pattern.findall(args_section)

        for arg in args:
            param, arg_type, description = arg
            description = self._format_description(description)
            default_value = self._get_default_value(description)

            self.params[param] = {
                "arg_type": arg_type,
                "description": description,
                "default_value": default_value,
            }

        return self._format_args()

    def get_examples(self) -> str:
        if self.docstring is None:
            return "No arguments found"

        pattern = re.compile(r"Example:.*?(?=\Z|Example:)", re.DOTALL)
        matches = pattern.findall(self.docstring)

        if matches == []:
            return None

        output = []
        for match in matches:
            innerOutput = ""
            pattern = re.compile(r">>>.*", re.DOTALL)
            innerMatches = pattern.findall(match)

            for innerMatch in innerMatches:
                innerOutput += innerMatch.strip()

            output.append(innerOutput)

        output = [
            _example_template.replace("{example}", example)
            for example in output
        ]

        self.examples = "".join(output)

        return self.examples

    def _get_default_value(self, line: str) -> str | None:
        """Extracts the default value from the line. Returns None if no default
            value is found.

        Args:
            line (str): Line from docstring to extract default value from.
        """

        pattern = r"Defaults to (.+)\."

        match_obj = re.search(pattern, line.strip())

        if match_obj:
            default_value = match_obj.group(1).strip()
            return f"{default_value}"

        return None

    def _format_description(self, arg: str) -> str:
        """Format the description of the argument by replace backticks and
            apostrophes with <code> tags.

        Args:
            arg (str): String expression to format.
        """

        # Normalize the whitespace in the arg
        arg = re.sub(r"\s+", " ", arg).strip()

        pattern = r"[`']"
        count = 0

        def replace(arg):
            nonlocal count
            count += 1
            return "<code>" if count % 2 != 0 else "</code>"

        return re.sub(pattern, replace, arg)

    def _format_args(self, template=_arg_template) -> str:
        """Format the arguments into a HTML template for use in Markdown files.

        Args:
            template (str, optional): HTML template to format the arguments.
        """

        output = ""

        for name, arg in self.params.items():

            default_arg = arg["default_value"]

            if default_arg is None:
                template = _arg_template_no_default

                output += template.format(
                    name=name,
                    arg_type=arg["arg_type"],
                    description=arg["description"],
                )
            else:
                output += template.format(
                    name=name,
                    arg_type=arg["arg_type"],
                    default_arg=default_arg,
                    description=arg["description"],
                )

        self.args = f"<ul>\n{output}</ul>\n"

        return self.args


def parse(cls_or_func: object | FunctionType) -> tuple[str, str, str]:
    """Parse the docstring of a class or function and return a tuple of strings:
        function, summary, args, and examples.

    Args:
        cls_or_func (object | FunctionType): Class or function to parse the
            docstring of.
    """

    parser = Parser(cls_or_func)
    parser.run()
    return parser.function, parser.summary, parser.args, parser.examples
