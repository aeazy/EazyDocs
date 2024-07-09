class Example:
    def __init__(
        self, val: str, string: str = "Test", num: int | float = None
    ) -> None:
        self.val = val
        self.string = string
        self.num = num

    def example_method(
        self, param: list, param2: str = None, param3: str = "Test"
    ) -> None:
        """Example method for <class Example>.

        Args:
            param (list): Example required argument.
                If `param=None` then...
            param2 (str, optional): Example default None argument. Defaults to None.
            param3 (str, optional): Example default str argument. Defaults to "Test".
        """

        pass
