from directory_printer.build_directory_structure import build_directory_structure


def test_empty_folder(fs):
    fs.create_dir('/example/dir')
    structure = build_directory_structure('/example/dir')
    assert structure.dir_name == 'dir'
    assert structure.files == []
    assert structure.subdirectories == []

def test_folder_with_file(fs):
    fs.create_dir('/example/dir')
    fs.create_file('/example/dir/foo.txt')
    structure = build_directory_structure('/example/dir')
    assert structure.files == ['foo.txt']
    assert structure.subdirectories == []

def test_folder_with_subfolder(fs):
    fs.create_dir('/example/dir')
    fs.create_dir('/example/dir/sub')
    fs.create_file('/example/dir/sub/a.txt')
    structure = build_directory_structure('/example/dir')
    assert structure.files == []
    assert len(structure.subdirectories) == 1
    subdir_structure = structure.subdirectories[0]
    assert subdir_structure.dir_name == 'sub'
    assert subdir_structure.files == ['a.txt']
    assert subdir_structure.subdirectories == []


# Could add further tests for
# - symlinks
# - invalid inputs like passing in the path of a file
