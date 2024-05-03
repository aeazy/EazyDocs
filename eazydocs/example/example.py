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

    def __format_df__(self) -> str:
        if self.data.shape[0] > 5:
            df = self.data[0:5]

        if self.data.shape[1] > 4:
            df = df.iloc[0:5, 0:4]

        return df.to_string()


df = DataFrame(
    {
        "col1": [i for i in range(0, 11)],
        "col2": [i for i in range(0, 11)],
        "col3": [i for i in range(0, 11)],
        "col4": [i for i in range(0, 11)],
        "col5": [i for i in range(0, 11)],
        "col6": [i for i in range(0, 11)],
    }
)
