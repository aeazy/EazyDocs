class Param:
    def __init__(self, param: str) -> None:
        self.parse_param(param)

    def parse_param(self, param: str) -> None:
        self.param = param.strip().split(":")
        self._name()
        self._arg_type()

    def _name(self) -> None:
        name = self.param[0].strip()

        self.name = name.replace("<b>", "").strip()

    def _arg_type(self) -> None:
        arg_type = self.param[1]
        arg_type = arg_type.split("</i>")[0]
        arg_type = arg_type.replace("<i>", "").strip()

        self.arg_type = arg_type
