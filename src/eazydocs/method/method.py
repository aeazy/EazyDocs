from collections import defaultdict

from .param import Param


class Method:
    def __init__(self, method: str) -> None:
        self.params = defaultdict(list)

        self.parse_method(method)

    def parse_method(self, method: str) -> None:
        method = method.strip()
        self.method = method.split("\n")

        self._name()
        self._parse_params()

    def _name(self) -> None:
        name = None

        while self.method:
            line = self.method.pop(0)

            if "<strong id=" in line:
                line = line.split(">")
                name = line[1].split("<")[0]
                self.name = name
                self.params[name] = dict()
                break

        self.name = name

    def _parse_params(self) -> None:
        if self.method is not None:
            while self.method:
                line = self.method.pop(0)

                if self._is_param(line):
                    param = Param(line)
                    name = param.name

                    description = self._parse_description()
                    self.params[self.name].update(
                        {f"{name}":dict(
                                arg_type=param.arg_type,
                                default_arg = param.default_arg,
                                description=description,
                            )
                        }
                    )

    def _is_param(self, arg: str) -> bool:
        if "<b>" not in arg:
            return False
        return True

    def _parse_description(self) -> str:
        line = self.method.pop(0)
        if "<li>" not in line:
            line = self.method.pop(0)
        description = line.split("<li>")[-1]
        description = description.replace("</li>", "")
        return description
