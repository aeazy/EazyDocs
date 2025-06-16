class Example:
    """Example method for <class Example>.

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
        self.val = val
        self.string = string
        self.num = num

    def example_method(
        self, param: list, param2: str = None, param3: str = "Test"
    ) -> None:
        """Example method for <class Example>.

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


from pandas import DataFrame
