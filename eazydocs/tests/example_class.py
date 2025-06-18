class Example:
    """Example method for `Example` class.

    Args:
        param (list): Example required argument. If `param=None` then... else if
            `param=[]` then...
        param2 (str, optional): Example default None argument. Defaults to None.
        param3 (str, optional): Example default str argument. Defaults to
            "Test".

    Examples:

    General

        >>> d
        col1     col2
        0       First
        1      Second

    With DataFrame

        >>> data = Data("data.csv")
        >>> data.df
        Date_Time_1          vo2_1 vo2_2
        2025-01-01 00:00:00    0.0   0.0
        2025-01-01 01:00:00    0.0   0.0
        2025-01-01 02:00:00    0.0   0.0
        ...
    """

    def __init__(
        self, val: str, string: str = "Test", num: int | float = None
    ) -> None:
        """Example initialization method for `Example` class.

        Args:
            val (str): Example required argument.
            string (str, optional): Example default string argument. Defaults to
                "Test".
            num (int | float, optional): Example default number argument.
                Defaults to None.
        """
        self.val = val
        self.string = string
        self.num = num

    def example_method(
        self, param: list, param2: str = None, param3: str = "Test"
    ) -> None:
        """Example updated method for Example class.

        Args:
            param (list): Example required argument. If `param=None` then...
                else if `param=[]` then...
            param2 (str, optional): Example default None argument. Defaults to
                None.
            param3 (str, optional): Example default str argument. Defaults to
                "Test".

        Examples:
        Read

            >>> d
        """

        pass

    def example_method2(
        self, param: list, param2: str = None, param3: str = "Test"
    ) -> None:
        """Example method2 for <class Example>.

        Args:
            param (list): Example required argument. If `param=None` then...
                else if `param=[]` then...
            param2 (str, optional): Example default None argument. Defaults to
                None.
            param3 (str, optional): Example default str argument. Defaults to
                "Test".

        Examples:
        Read

            >>> d
        """

        pass
