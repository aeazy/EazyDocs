from pandas import DataFrame
from subprocess import run

from eazydocs import generate_example


def get_dataframe(
    shape: tuple[int, int],
    column_titles: list[str] = None,
    row_data: list[str | int] = None,
) -> DataFrame:
    num_columns, num_rows = shape

    if column_titles != None:
        columns = column_titles
    else:
        columns = [f"col_{i}" for i in range(1, num_columns + 1)]

    if row_data != None:
        row = row_data
    else:
        row = [i for i in range(0, num_rows + 1)]

    data = dict()

    for column in columns:
        data.update({column: row})

    df = DataFrame(data)

    return df


e = generate_example(
    DataFrame({"col1": [i for i in range(0, 10)]}),
    # append_to_file=True,
    # filename="readme2",
    # filepath=Path("D:/", "software", "eazydocs", "tests"),
    # method_name="generate_example",
)

# print(e)

# run(["clip.exe"], input=e.encode("utf-8"))
