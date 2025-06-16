class _Parser(type):
    """Eazydocs Parser Metaclass utilized to parse methods and their docstrings.

    This metaclass is responsible for parsing the docstring of a method to
    extract arguments, parameters, examples, and formatted arguments. It is
    used in the MethodType class to create an instance with the parsed method.
    """

    def __call__(self, *args, **kwds):
        """The metaclass for the MethodType class.

        This metaclass is used to create a new instance of the class and set the
        attributes based on the provided keyword arguments.

        A single argument is expected, which is the method to be parsed.

        Raises:
            TypeError: If no arguments are provided to the MethodType class.

        Returns:
            MethodType: An instance of the MethodType class with the parsed
                method.

        Notes:
            - The method should be a callable object, such as a function or a
            method, and it should have a docstring that follows the expected
            format for parsing arguments, parameters, and examples.
            - An instance of MethodType is created with the parsed method,
            and its attributes such as `args`, `params`, `examples`, and
            `args_fmtd` are set based on the parsed information from the
            method's docstring.
        """
        if args is None:
            raise TypeError("MethodType requires a method as an argument.")
        
        arg = args[0]
        self.method = arg

        from eazydocs.core.method_type import MethodType

        instance: MethodType = super().__call__(*args, **kwds)

        instance.summary = instance._get_summary()
        instance.args = instance._get_args()
        instance.params = instance._get_params()
        instance.function = instance._get_function_signature()
        instance.examples = instance._get_examples()
        instance.args_fmtd = instance._format_args()

        return instance
