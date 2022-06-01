from cli_test_helpers import shell


def test_help():
    result = shell('gendiff -h')
    assert result.exit_code == 0


def test_gendiff_default():
    result = shell(
        'gendiff '
        'tests/fixtures/nested/file1.json '
        'tests/fixtures/nested/file2.yaml'
    )
    assert result.exit_code == 0


def test_gendiff_plain():
    result = shell(
        'gendiff -f plain '
        'tests/fixtures/nested/file1.json '
        'tests/fixtures/nested/file2.yaml'
    )
    assert result.exit_code == 0


def test_gendiff_stylish():
    result = shell(
        'gendiff -f stylish '
        'tests/fixtures/nested/file1.json '
        'tests/fixtures/nested/file2.yaml'
    )
    assert result.exit_code == 0


def test_gendiff_json():
    result = shell(
        'gendiff -f json '
        'tests/fixtures/nested/file1.json '
        'tests/fixtures/nested/file2.yaml'
    )
    assert result.exit_code == 0


def test_gendiff_wrong_type():
    result = shell(
        'gendiff '
        'tests/fixtures/nested/result_nested_plain '
        'tests/fixtures/nested/file2.yaml'
    )
    assert "TypeError: Unknown file type!" in result.stderr


def test_gendiff_wrong_format():
    result = shell(
        'gendiff -f yaml '
        'tests/fixtures/nested/file1.json '
        'tests/fixtures/nested/file2.yaml'
    )
    assert '-f/--format: invalid choice' in result.stderr
