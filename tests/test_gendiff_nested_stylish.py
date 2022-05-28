import pytest
from gendiff import generate_diff


@pytest.fixture
def expected():
    with open('tests/fixtures/nested/result_nested_stylish', 'r') as expected:
        return expected.read()


def test_diff_json(expected):
    assert generate_diff('tests/fixtures/nested/file1.json',
                         'tests/fixtures/nested/file2.json') == expected


def test_diff_yaml(expected):
    assert generate_diff('tests/fixtures/nested/file1.yaml',
                         'tests/fixtures/nested/file2.yaml') == expected

    assert generate_diff('tests/fixtures/nested/file1.yml',
                         'tests/fixtures/nested/file2.yml') == expected


def test_error():
    with pytest.raises(TypeError):
        generate_diff('tests/fixtures/nested/result_nested_plain',
                      'tests/fixtures/nested/result_nested_stylish')
