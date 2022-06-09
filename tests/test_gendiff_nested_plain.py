import pytest
from gendiff import generate_diff
from gendiff.format.output import PLAIN


@pytest.fixture
def expected():
    with open('tests/fixtures/nested/result_nested_plain', 'r') as result:
        return result.read()


def test_diff_json(expected):
    assert generate_diff('tests/fixtures/nested/file1.json',
                         'tests/fixtures/nested/file2.json',
                         PLAIN) == expected


def test_diff_yaml(expected):
    assert generate_diff('tests/fixtures/nested/file1.yaml',
                         'tests/fixtures/nested/file2.yaml',
                         PLAIN) == expected

    assert generate_diff('tests/fixtures/nested/file1.yml',
                         'tests/fixtures/nested/file2.yml',
                         PLAIN) == expected
