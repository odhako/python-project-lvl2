import pytest
from json import load as file_load
from json import dumps as json_dumps
from gendiff import generate_diff
from gendiff.format.output import JSON


@pytest.fixture
def expected():
    with open(
            'tests/fixtures/nested/result_nested.json', 'r') as result:
        return json_dumps(file_load(result))


def test_diff_json(expected):
    assert generate_diff('tests/fixtures/nested/file1.json',
                         'tests/fixtures/nested/file2.json',
                         JSON)


def test_diff_yaml(expected):
    assert generate_diff('tests/fixtures/nested/file1.yaml',
                         'tests/fixtures/nested/file2.yaml',
                         JSON)

    assert generate_diff('tests/fixtures/nested/file1.yml',
                         'tests/fixtures/nested/file2.yml',
                         JSON)


def test_error():
    with pytest.raises(TypeError):
        generate_diff('tests/fixtures/nested/result_nested_plain',
                      'tests/fixtures/nested/result_nested_stylish',
                      JSON)

# TODO: Переделать тест
