from eazydocs.core import create_md_file, get_documentation
from eazydocs.core.class_type import ClassType
from eazydocs.core.functions import get_example, update_md_file
from eazydocs.markdown.updater import Updater
from eazydocs.markdown.writer import Writer
from eazydocs.tests.example_class import Example
from eazydocs.tests.example_methods import (
    set_plot_title,
    no_docstring,
    make_subplot,
)


# docs = create_md_file(Example, "README", path="TEST")

# updater = Updater(Example, "README.md", "TEST")


doc = get_documentation(get_example)

