from eazydocs.core import create_md_file, get_documentation
from eazydocs.core.class_type import ClassType
from eazydocs.markdown.updater import Updater
from eazydocs.tests.example_class import Example
from eazydocs.tests.example_methods import (
    set_plot_title,
    no_docstring,
    make_subplot,
)


# docs = create_md_file(Example, "README.md", path="TEST")

# updater = Updater(Example, "README.md", "TEST")
updater = Updater(Example.example_method, "README.md", "TEST")
