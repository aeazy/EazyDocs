from pandas import DataFrame

"""eazydocs.example streamlines generating codeblocks for pandas DataFrames.
"""


class Example:
    def __init__(self, code: str, data: DataFrame, df_shape: list[int]) -> None:
        if len(df_shape) != 2:
            raise ValueError("Length of list provided for 'df_shape' must be exactly 2 integers: [num_rows, num_columns]")

        self.data = data
        self.code = code

        self.rows = df_shape[0]
        self.columns = df_shape[1]

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
