from eazydocs.core.class_type import ClassType
from eazydocs.tests.example_class import Example
from eazydocs.tests.example_methods import (
    set_plot_title,
    no_docstring,
    make_subplot,
)


cls = ClassType(Example)
cls.parse()
# print(cls.output)
