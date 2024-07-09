from eazydocs import update_md_file, read_md_file, create_md_file
from eazydocs.tests.example_methods import (
    set_plot_title,
    no_docstring,
    make_subplot,
)
from eazydocs.tests.example_class import Example

from eazydocs.markdown import Parser

filepath = "C:/Software/EazyDocs-v2/eazydocs/tests"

# create_md_file(Example)

# r = update_md_file(Example, "readme")

s = read_md_file("readme")
parser = Parser(s)
print(parser.methods)
