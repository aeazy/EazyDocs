from dataclasses import dataclass
import subprocess


@dataclass
class Parameter:
    name: str
    description: str


@dataclass
class ParsedParameter:
    name: str
    type: str
    default_value: str


class Generator:
    def __init__(self, parameters: list[Parameter], function: str) -> None:
        self.parameters = parameters

        self.function = self.__generate_function__(function)
        self.description = "<ul style='list-style: none'>"

        self.run()

    def run(self) -> None:
        for paramater in self.parameters:
            parsed_parameter = self.__parse_parameter_name__(paramater.name)
            self.__append_function__(parsed_parameter)
            formatted_description = self.__format_parameter_description__(paramater.description)
            self.description += self.__generate_parameter_documentation__(parsed_parameter, formatted_description)

        self.description += "</ul>\n<hr />"
        self.__format_function__()

        output = f"{self.function}\n\n> Parameters\n{self.description}"

        subprocess.run(["clip.exe"], input=output.lstrip().encode("utf-8"))

        # print(f"\n{self.function}\n")

    def __parse_parameter_name__(self, name: str) -> ParsedParameter:
        parsed_name = name.split(":")
        name = parsed_name[0].strip()
        type = parsed_name[1].strip()

        try:
            default_value = parsed_name[2].strip()
        except IndexError:
            default_value = ""

        if default_value == "":
            default_value = None

        return ParsedParameter(name, type, default_value)

    def __generate_function__(self, function: str) -> str:
        function_id = function.replace("_", "-")
        function = f"<strong id='{function_id}'>{function}</strong>("
        return function

    def __append_function__(self, parameter: ParsedParameter) -> str:
        if parameter.default_value == None:
            self.function += f"<b>{parameter.name}</b>, "
        else:
            self.function += f"<b>{parameter.name}</b>=<i>{parameter.default_value}</i>, "

    def __format_function__(self) -> None:
        self.function = self.function.removesuffix(", ")
        self.function += ")"

    def __format_parameter_description__(self, description: str) -> str:
        description = description.replace("{", "<code>").replace("}", "</code>").strip()
        return description

    def __generate_parameter_documentation__(self, parameter: ParsedParameter, description: str) -> str:
        if parameter.default_value == None:
            template = self.__parameter_template__(True)
            documentation = template.replace("{name}", parameter.name).replace("{type}", parameter.type).replace("{description}", description)

        else:
            template = self.__parameter_template__()

            documentation = (
                template.replace("{name}", parameter.name)
                .replace("{type}", parameter.type)
                .replace("{default_value}", parameter.default_value)
                .replace("{description}", description)
            )

        return documentation

    def __parameter_template__(self, required: bool = False) -> str:
        if required:
            return """<li>
        <b>{name} : <i> {type}</i></b>
        <ul style="list-style: none">
            <li>{description}</li>
        </ul>
    </li>
    """

        return """<li>
        <b>{name} : <i> {type}, default {default_value}</i></b>
        <ul style="list-style: none">
        <li>{description}</li>
        </ul>
    </li>
    """
