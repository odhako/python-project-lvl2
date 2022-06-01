### Hexlet tests and linter status:
[![Actions Status](https://github.com/odhako/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/odhako/python-project-lvl2/actions)
[![Tests and linter](https://github.com/odhako/python-project-lvl2/actions/workflows/test-and-linter.yml/badge.svg)](https://github.com/odhako/python-project-lvl2/actions/workflows/test-and-linter.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/1721476434a5efe8ca48/maintainability)](https://codeclimate.com/github/odhako/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1721476434a5efe8ca48/test_coverage)](https://codeclimate.com/github/odhako/python-project-lvl2/test_coverage)

## Gendiff
Diff generator for with command line interface.
Supports json and yaml files.

#### Manual installation:
- Install poetry https://python-poetry.org/docs/master/#installing-with-the-official-installer
- Download or clone source code
- Open directory in a terminal
- `poetry install`
- `poetry build`
- `python3 -m pip install --user dist/*.whl`

#### Usage:
`gendiff first_file_path second_file_path`

`-f --format` `{stylish, plain, json}` - choose format. Default is stylish.

### Demo:
- `gendiff file1 file2` - plain json files: [asciinema](https://asciinema.org/a/495168)
- `gendiff file1 file2` - plain json and yaml files: [asciinema](https://asciinema.org/a/495671)
- `gendiff file1 file2` - nested files: [asciinema](https://asciinema.org/a/497757)
- `gendiff -f plain file1 file2` - plain style [asciinema](https://asciinema.org/a/497782)
- `gendiff -f json file1 file2` - json format output [asciinema](https://asciinema.org/a/498043)
