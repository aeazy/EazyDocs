from .param import Param


class Method:
    def __init__(self, method: str) -> None:
        self.params = dict()

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
                break

        self.name = name

    def _parse_params(self) -> None:
        if self.method is not None:
            while self.method:
                line = self.method.pop(0)

                if self._is_param(line):
                    param = Param(line)
                    self.params.update({param.name: param.arg_type})

    def _is_param(self, arg: str) -> bool:
        if "<b>" not in arg:
            return False
        return True
