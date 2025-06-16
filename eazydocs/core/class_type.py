from inspect import getmembers, isfunction, ismethod


class ClassType:
    """ClassType is a class that represents a Python class and its methods.
    It is used to generate documentation for the class and its methods.

    Args:
        cls (object): The class to be documented.
        include_examples (bool, optional): Whether to include examples in the
            documentation. Defaults to True.
    Returns:
        None

    Example:
        Example output:

        ## ClassType

        {function signature}

        {summary}

        > Parameters:

        {...args}

        ### Class Methods

        {Table of Contents}

        {...methods}
    """

    def __init__(
        self,
        cls: object,
        include_methods: bool = True,
        include_private_methods: bool = False,
        include_examples: bool = True,
    ):
        # Initialize the ClassType object.
        self.cls = cls
        self.include_methods = include_methods
        self.include_private_methods = include_private_methods
        self.include_examples = include_examples

        self.name: str = cls.__name__
        self.id = self.name.replace("_", "-")
        self.summary = None
        self.methods: list = []
        self.table_of_contents = []

        self._get_docstring()
        self._parse_class_members()

    def _get_docstring(self) -> None:
        """Get the docstring of the class."""
        docstring = self.cls.__doc__
        if docstring is None:
            docstring = self.cls.__init__.__doc__
        self.docstring = docstring.strip() if docstring else None

    def _parse_class_members(self) -> None:
        """Parse the members of the class."""
        for name, member in getmembers(self.cls):
            if ismethod(member) or isfunction(member):
                if name == "__init__":
                    self._parse_class_docstring(member)
                elif self.include_methods:
                    if self.include_private_methods:
                        self.methods.append(
                            MethodType(
                                member,
                                include_examples=self.include_examples,
                            )
                        )
                    elif not name.startswith("_"):
                        self.methods.append(
                            MethodType(
                                member,
                                include_examples=self.include_examples,
                            )
                        )

    def _parse_class_docstring(self, method: FunctionType) -> str:
        """Parse the docstring of the class and extract the summary,
        arguments, and examples.
        """

        function, self.summary, self.args, self.examples = parse(method)

        self.function = self._format_function(function)
        return self.format_docs()

    def __repr__(self):
        return f"""ClassType(
        name={self.name}, 
        function={self.function},
        id={self.id}, 
        summary={self.summary},
    )"""

    def _format_function(self, function: str) -> str:
        return function.replace("--init--", self.name).replace(
            "__init__", self.name
        )

    def _format_docs(self) -> str:
        docs = f"## {self.name}\n\n"

        docs += f"{self.function}\n\n{self.summary}\n\n"

        if self.args:
            docs += f"> Parameters:\n\n{self.args}\n"

        if self.methods != []:
            docs += "### Class Methods\n\n"
            if self.include_table_of_contents:
                docs += self._build_table_of_contents()
                docs += "\n"

            docs += "\n".join(
                [method.format_docs() for method in self.methods]
            )

        return docs

    def get_table_of_contents(self) -> str:
        """Generate a table of contents for the class methods."""
        if not self.methods:
            return ""

        table_of_contents = ""
        for method in self.methods:
            table_of_contents += f"- [{method.name}](#{method.id})\n"
        return table_of_contents
