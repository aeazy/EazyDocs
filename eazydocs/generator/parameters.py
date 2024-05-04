from dataclasses import dataclass
from inspect import signature

from generator.method import Method
from generator.templates import DEFAULT_ARG_TEMPLATE, TEMPLATE


@dataclass
class Param:
    name: str
    arg_type: str
    default_arg: str


class Parameters(Method):
    def __init__(self, method: object) -> None:
        super().__init__(method.__name__)
        self.generate(method)

    def generate(self, method: object) -> None:
        self.fn = self.__generate_function__(method.__name__)

        params = self.get_params_output(method)

        fn = self.fn.removesuffix(", ") + ")"

        self.params = f"{fn}\n{params}"

    def __repr__(self) -> str:
        return self.params

    def get_params_output(self, method: object) -> str:
        params = self.__get_params__(method)

        if params == []:
            return ""
        blockquote = "> Parameters"
        output = f"\n{blockquote}\n\n<ul style='list-style: none'>\n"

        for param in params:
            output += self.__fmt_param__(param)

        output += "</ul>"

        return output

    def __get_params__(self, method: object) -> list[Param]:
        sig_params = signature(method).parameters
        parameters_filtered = [param for param in sig_params.keys() if param != "self"]

        parameters = [sig_params.get(param) for param in parameters_filtered]

        params = list()

        for param in parameters:
            param = str(param).split(":")
            param_name = param[0].strip()
            param_arg_type = param[1].strip()

            if "=" in param_arg_type:
                param_arg_type_split = param_arg_type.split("=")
                param_arg_type = param_arg_type_split[0].strip()
                param_default_arg = param_arg_type_split[-1].strip()
            else:
                param_default_arg = ""

            params.append(Param(param_name, param_arg_type, param_default_arg))

        return params

    def __fmt_param__(self, param: Param) -> None:
        if param.default_arg == "":
            template = TEMPLATE
        else:
            template = DEFAULT_ARG_TEMPLATE

        if "None" in param.default_arg:
            template = template.replace("{name}", param.name).replace("{type}", param.arg_type).replace("{default_arg}", f"optional")
            param.default_arg = "_NoDefault.no_default"
        else:
            template = (
                template.replace("{name}", param.name).replace("{type}", param.arg_type).replace("{default_arg}", f"default {param.default_arg}")
            )

        self.__append_param__(param)

        return template

    def __append_param__(self, param: Param) -> None:
        name = param.name
        default_arg = param.default_arg

        to_append = f"<b>{name}</b>"

        if default_arg != "":
            to_append += f"<i>={default_arg}</i>, "
        else:
            to_append += ", "

        self.fn += to_append

