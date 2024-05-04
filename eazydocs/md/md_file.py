from pathlib import Path


class MDFile:
    def __init__(self, filename: str = None, to_append: str = None, output_dir: None | Path = None) -> None:
        if to_append == None:
            raise ValueError("Markdown() missing 1 required positional argument: 'to_append'")

        if output_dir != None:
            self.path = self.__set_path_attr__(output_dir)
        else:
            self.path = self.__set_path_attr__()

        if filename != None:
            filename = self.__check_filename__(filename)
            self.append(filename, to_append)
        else:
            filename = self.__set_filename__()
            self.append(filename, to_append)

    def append(self, filename: str, to_append: str) -> None:
        with open(filename, "+a") as f:
            f.write(to_append)

        print(f"Succesfully updated {filename}.")

    def __set_path_attr__(self, path: None | Path = None) -> None:
        if path != None:
            self.p = path
            self.cwd = path
        else:
            p = Path()
            self.p = p
            self.cwd = p.cwd()

    def __check_filename__(self, filename: str) -> str:
        filename = filename.strip()

        if filename[-3:] != ".md":
            filename += ".md"

        return filename

    def __set_filename__(self) -> str:
        if Path(self.cwd, "README.md").exists():
            md_files = list(self.p.glob("README_*.md"))

            try:
                last_file = str(md_files.pop())
                last_filename = last_file.replace(".md", "").split("_")
                last_file_num = int(last_filename[-1])
                filename = f"README_{last_file_num+1}.md"
            except IndexError:
                filename = "README_2.md"

        else:
            filename = "README.md"

        self.__create_file__(filename)

        return filename

    def __create_file__(self, filename: str) -> None:
        path = Path(self.p, filename)

        with open(path, "w") as f:
            f.write("")

        print(f"Created markdown file ({filename}) at {path}.")
