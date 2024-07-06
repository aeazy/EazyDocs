from pathlib import Path

from eazydocs.method import Method

from .markdown import Markdown


class Updater(Markdown):
    def __init__(
        self,
        filename: str,
        filepath: str | Path = None,
        method_to_update: str = None,
    ) -> None:
        super().__init__(filename, filepath)

        if method_to_update is None:
            raise TypeError("Missing required argument 'method'")

        self.updated_method = method_to_update

        self.method = Method(method_to_update)

        self.update_method()

    def update_method(self) -> None:
        self.load()

        method_name = self.method.name.replace("_", "-")
        method_id = f"id='{method_name}'"

        method_start = self.contents.find(method_id) - 8
        method_end = self.contents[method_start:].find("<hr>")

        self._compare_method(
            self.contents[method_start : method_start + method_end]
        )

        contents_before = self.contents[:method_start]
        contents_after = self.contents[method_end:]

        new_contents = contents_before + self.updated_method

    # TODO: Check for old method descriptions

    def _compare_method(self, current_method: str) -> None:
        method = Method(current_method)
        current_params = method.params.get(method.name)
        print(current_params)

        