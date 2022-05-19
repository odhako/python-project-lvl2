import pytest
from gendiff import generate_diff


@pytest.fixture
def expected():
    with open('tests/fixtures/result_file1_file2.txt', 'r') as expected:
        return expected.read()


def test_diff_json(expected):
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected


def test_diff_yaml(expected):
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == expected
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == expected


def test_error():
    with pytest.raises(TypeError):
        generate_diff('tests/fixtures/result_file1_file2.txt', 'tests/fixtures/result_file1_file2.txt')
