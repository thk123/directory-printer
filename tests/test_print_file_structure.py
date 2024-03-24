from directory_printer.DirectoryStructure import DirectoryStructure
from directory_printer.print_directory_structure import build_directory_structure_output


def test_print_file_only_structure():
    file_only_structure =  DirectoryStructure(
        dir_name='root',
        files=['foo.txt', 'bar.txt'], subdirectories=[]
    )
    output = build_directory_structure_output(file_only_structure)
    assert output == ['root/', '    foo.txt', '    bar.txt']

def test_files_and_folders():
    files_and_folders =  DirectoryStructure(
        dir_name='root',
        files=['foo.txt', 'bar.txt'], subdirectories=[
            DirectoryStructure(dir_name='subdir', files= ['nested.txt'], subdirectories=[])
        ]
    )
    output = build_directory_structure_output(files_and_folders)
    assert output == ['root/',
                      '    foo.txt',
                      '    bar.txt',
                      '    subdir/',
                      '        nested.txt']

# TODO: could add additional tests here
# - doubly nested folder
# - only folder no files in root
