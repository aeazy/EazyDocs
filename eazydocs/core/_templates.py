"""eazydocs.core._templates.py

This module contains templates for generating documentation pages.
"""

ARG_TEMPLATE = """    <li>
        <b>{name} : <i>{arg_type}, {default_arg}</i></b>
        <ul style='list-style: none'>
            <li>{description}</li>
        </ul>
    </li>
"""

ARG_TEMPLATE_NODEFAULT = """    <li>
        <b>{name} : <i>{arg_type}</i></b>
        <ul style='list-style: none'>
            <li>{description}</li>
        </ul>
    </li>
"""


EXAMPLE_TEMPLATE = """
```python
{example}
```"""
