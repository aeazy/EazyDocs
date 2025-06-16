from eazydocs.core.method_type import MethodType

from eazydocs.tests.example_class import Example
from eazydocs.tests.example_methods import (
    set_plot_title,
    no_docstring,
    make_subplot,
)

method = MethodType(Example)

# print(method.__dict__.keys())
# print(method)
method.parse()
