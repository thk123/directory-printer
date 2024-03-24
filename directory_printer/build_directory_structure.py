import os
from directory_printer.DirectoryStructure import DirectoryStructure


def build_directory_structure(root_directory: str | os.PathLike[str]) -> DirectoryStructure:
    # TODO: here there should be robust error checking that root directory
    # is indeed a directory
    # TODO: Handle symlinks etc
    files = [file_name
             for file_name in os.listdir(root_directory)
             if os.path.isfile(os.path.join(root_directory, file_name))]
    subdirectory_names = [file_name
             for file_name in os.listdir(root_directory)
             if os.path.isdir(os.path.join(root_directory, file_name))]
    subdirectory_structures = [build_directory_structure(os.path.join(root_directory, subdirectory_name))
                      for subdirectory_name in subdirectory_names]

    return DirectoryStructure(
        dir_name=os.path.basename(root_directory),
        files=files,
        subdirectories=subdirectory_structures
    )
