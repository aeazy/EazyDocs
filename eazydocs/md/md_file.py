from pathlib import Path


class MDFile:
    def __init__(self, filename: str = None, to_append: str = None, filepath: Path | str = None) -> None:
        if to_append == None:
            raise ValueError("Markdown() missing 1 required positional argument: 'to_append'")
        else:
            self.to_append = to_append

        if filepath != None:
            self.path = self.__set_path_attr__(filepath)
        else:
            self.path = self.__set_path_attr__()

        if filename != None:
            self.filename = self.__check_filename__(filename)
            # self.append(filename, to_append)
        else:
            self.filename = self.__set_filename__()
            # self.append(filename, to_append)

    def append(self) -> None:
        with open(self.filename, "+a") as f:
            f.write(self.to_append)

        print(f"Succesfully updated {self.filename}.")

    def append_to_param(self, method_name: str) -> None: 
        before, after = self.__slice_contents_at_insert_position__(method_name)
        to_append = self.__generate_output_str__(before, after)
        
        with open(self.filename, 'w') as f:
            f.write(to_append)
        
        print(f"Succesfully updated '{method_name}' in '{self.filename}'.")

                
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

    def __slice_contents_at_insert_position__(self, method_name: str) -> tuple[str, str]:
        with open(self.filename, "r+") as f:
            contents = f.read()

            if contents.__contains__(method_name) is False:
                raise ValueError(f"Unable to find {method_name} in {filename}. Confirm the spelling is correct, as well as the filepath: {file}")

            method_start = contents.find(f">{method_name}<")
            next_method_start = contents.find("<strong", method_start)
            
            return (contents[0:next_method_start], contents[next_method_start:-1])

    def __generate_output_str__(self, s1: str, s2: str) -> str:
        output = s1 + "\n\n> Example\n\n" + self.to_append + "\n" + s2
        return output