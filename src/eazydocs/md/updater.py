from pathlib import Path

from eazydocs.method import Method
from eazydocs.generator.templates import DEFAULT_ARG_TEMPLATE

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

        self.method_to_update = method_to_update

        self.update_method()

    def update_method(self) -> None:
        self._get_method(self.method_to_update)

        self.load()

        method_name = self.method.name.replace("_", "-")
        method_id = f"id='{method_name}'"

        method_start = self.contents.find(method_id) - 8
        method_end = self.contents[method_start:].find("<hr>")

        self._copy_description(
            self.contents[method_start : method_start + method_end]
        )

        contents_before = self.contents[:method_start]
        contents_after = self.contents[(method_start + method_end) :]

        new_contents = (
            contents_before + self.updated_method + "\n" + contents_after
        )

        with open(self.filename, "w") as f:
            f.write(new_contents)

    def _get_method(self, new_method: str) -> None:
        method = Method(new_method)
        name = method.name

        self.method = method
        self.params: dict = method.params.get(name)

    def _copy_description(self, current_method: str) -> None:
        method = Method(current_method)
        current_params: dict = method.params.get(method.name)

        for key, val in self.params.items():
            old_param = current_params.get(key)

            if old_param is not None:
                self.params[key]["description"] = old_param["description"]

        self._fmt_method()

    def _fmt_method(self) -> None:
        updated_method = self.method_to_update.split("> Parameters")[0]
        updated_method += "> Parameters\n\n"

        for key, val in self.params.items():
            updated_method += "<ul style='list-style: none'>\n"

            default_arg = val.get("default_arg")

            if default_arg is None:
                default_arg = "optional"

            template = DEFAULT_ARG_TEMPLATE

            template = (
                template.replace("{name}", key)
                .replace("{type}", val.get("arg_type"))
                .replace("{default_arg}", default_arg)
                .replace("{description}", val.get("description"))
            )
            template = template.strip()
            template += "\n</ul>\n"

            updated_method += template

        self.updated_method = updated_method

        # TODO: Get docstring to create Method
