from praudio.utils import extract_extension_from_file, add_extension_to_file


def test_file_extension_is_extracted_correctly():
    extension = extract_extension_from_file("a/dummy/file.mp3")
    assert extension == "mp3"


def test_extension_is_added_to_file():
    file_with_extension = add_extension_to_file("a/dummy/file", "wav")
    assert file_with_extension == "a/dummy/file.wav"