import os

from praudio.utils import extract_extension_from_file, \
    add_extension_to_file, remove_extension_from_file, create_dir_hierarchy, \
    create_dir_hierarchy_from_file


def test_file_extension_is_extracted_correctly():
    extension = extract_extension_from_file("a/dummy/file.mp3")
    assert extension == "mp3"


def test_extension_is_added_to_file():
    file_with_extension = add_extension_to_file("a/dummy/file", "wav")
    assert file_with_extension == "a/dummy/file.wav"


def test_extension_is_removed_from_file():
    file_without_extension = remove_extension_from_file("a/dummy/file.wav")
    assert file_without_extension == "a/dummy/file"


def test_dir_hierarchy_is_created():
    create_dir_hierarchy("dummy/dummy2/dummy3")
    assert os.path.isdir("dummy/dummy2/dummy3")
    os.removedirs("dummy/dummy2/dummy3")


def test_dir_hierarchy_is_created_for_file():
    create_dir_hierarchy_from_file("dummy/dummy2/dummy3.wav")
    assert os.path.isdir("dummy/dummy2/")
    assert not os.path.isdir("dummy/dummy2/dummy3.wav")
    os.removedirs("dummy/dummy2/")