import pytest
from gendiff import generate_diff, stylish


@pytest.fixture
def expected():
    with open('tests/fixtures/plain/result_plain', 'r') as expected:
        return expected.read()


def test_diff_json(expected):
    assert stylish(generate_diff('tests/fixtures/plain/file1.json', 'tests/fixtures/plain/file2.json')) == expected


def test_diff_yaml(expected):
    assert stylish(generate_diff('tests/fixtures/plain/file1.yaml', 'tests/fixtures/plain/file2.yaml')) == expected
    assert stylish(generate_diff('tests/fixtures/plain/file1.yml', 'tests/fixtures/plain/file2.yml')) == expected


def test_error():
    with pytest.raises(TypeError):
        stylish(generate_diff('tests/fixtures/plain/result_plain', 'tests/fixtures/plain/result_plain'))
