from eazydocs.core import create_md_file, get_documentation
from eazydocs.core.class_type import ClassType
from eazydocs.tests.example_class import Example
from eazydocs.tests.example_methods import (
    set_plot_title,
    no_docstring,
    make_subplot,
)


docs = create_md_file(set_plot_title, "r", path="TEST")

# print(cls.output)
