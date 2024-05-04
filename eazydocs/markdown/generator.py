class Generator:
    def __init__(self, method: None | str = None, parameters: None | list[str] = None) -> None:
        if method == None and parameters == None:
            raise TypeError("Missing 2 required positional arguments: 'method' and 'parameters'")
        pass


