from gendiff import generate_diff


def test_diff_files():
    with open('tests/fixtures/result_file1_file2.txt', 'r') as expected:
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected.read()
