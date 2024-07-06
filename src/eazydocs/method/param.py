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

        if "," in arg_type:
            arg_split = arg_type.split(",")
            self.arg_type = arg_split[0]
            self._set_default_arg(arg_split[-1])
        else:
            self.arg_type = arg_type
            self.default_arg = None

    def _set_default_arg(self, arg: str) -> None:
        arg = arg.replace("default", "").strip()
        # try:
        #     if "int" in self.arg_type:
        #         arg = int(arg)
        # except ValueError:
        #     arg = float(arg)
        self.default_arg = arg
