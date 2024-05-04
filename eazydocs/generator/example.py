from pandas import DataFrame

"""eazydocs.example streamlines generating codeblocks for pandas DataFrames.
"""


class Example:
    def __init__(self, code: str, data: DataFrame, num_rows: int = 5, num_columns: int = 5) -> None:
        self.code = code
        self.data = data
        self.rows = num_rows
        self.columns = num_columns

        self.get_example()

    def get_example(self) -> None:
        bash = "```"
        df = self.__format_df__()

        self.output = f"{bash}\n>>> {self.code}\n{df}\n{bash}"

    def __repr__(self) -> str:
        return self.output

    def __format_df__(self) -> str:
        df = self.data

        if self.data.shape[0] > self.rows:
            df = df[0 : self.rows]

        if self.data.shape[1] > self.columns:
            df = df.iloc[0 : self.columns, 0 : self.columns]

        return df.to_string()
