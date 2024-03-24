class DirectoryStructure:
    def __init__(
        self,
        dir_name: str,
        files: list[str],
        subdirectories: list["DirectoryStructure"],
    ) -> None:
        # TODO: data validation on these inputs:
        # - dir name is non empty valid folder name
        # - subdirectories does not contain a cycle
        self.dir_name = dir_name
        self.files = files
        self.subdirectories = subdirectories
