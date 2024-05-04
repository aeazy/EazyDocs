from pandas import DataFrame

"""eazydocs.example streamlines generating codeblocks for pandas DataFrames.
"""


class Example:
    def __init__(self, code: str, data: DataFrame) -> None:
        self.code = code
        self.data = data

        self.get_example()

    def get_example(self) -> None:
        bash = "```"
        df = self.__format_df__()

        self.output = f"{bash}\n>>> {self.code}\n{df}\n{bash}"

    def __repr__(self) -> str:
        return self.output

    def __format_df__(self) -> str:
        df = self.data

        if self.data.shape[0] > 5:
            df = df[0:5]

        if self.data.shape[1] > 4:
            df = df.iloc[0:5, 0:4]

        return df.to_string()
