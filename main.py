from eazydocs import (
    update_md_file,
    read_md_file,
    create_md_file,
    get_method_docs,
)
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

get_method_docs(set_plot_title, True)
