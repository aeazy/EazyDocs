

class Method:
    def __init__(self, method_name: str) -> None:
        self.fn = self.__generate_function__(method_name)
    
    def __generate_function__(self, method: str) -> str:
        method = method.strip()
        method_id = method.replace("_", "-")
        return f"<strong id='{method_id}'>{method}</strong>("
