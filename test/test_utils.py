from praudio.utils import extract_extension


def test_file_extension_is_extracted_correctly():
    extension = extract_extension("a/dummy/file.mp3")
    assert extension == "mp3"