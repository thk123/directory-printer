from directory_printer.DirectoryStructure import DirectoryStructure

INDENT_WIDTH = 4


def _indent_line(line: str, indentation: int):
    indent = " " * (indentation * INDENT_WIDTH)
    return indent + line


def _build_directory_structure_output(
    directory_structure: DirectoryStructure, current_indentation: int
):
    lines: list[str] = []
    lines.append(_indent_line(directory_structure.dir_name + "/", current_indentation))
    for file_name in directory_structure.files:
        lines.append(_indent_line(file_name, current_indentation + 1))

    # Question: this algorithm is recurssive - might run into issues on deeply nested
    # directories
    for subdirectory in directory_structure.subdirectories:
        subdirectory_lines = _build_directory_structure_output(
            subdirectory, current_indentation + 1
        )
        lines.extend(subdirectory_lines)
    return lines


def build_directory_structure_output(
    directory_structure: DirectoryStructure,
) -> list[str]:
    """
    Given a directory structure, produce a structured output as a list
    of printable lines
    """
    # Question: do we care about the order in which the files / folders are printed
    # Based on provided input, did files first then any folders
    return _build_directory_structure_output(directory_structure, current_indentation=0)


def print_directory_structure_output(directory_structure: DirectoryStructure):
    output = build_directory_structure_output(directory_structure)
    for line in output:
        print(line)
