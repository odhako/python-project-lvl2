from gendiff.diff_tree_generator import make_inner_diff
from gendiff.format.output import form_output, STYLISH
from json import loads as json_loads
from yaml import safe_load as yaml_loads
from os.path import splitext


def read_file(file_path):
    if splitext(file_path)[1] == '.json':
        file_format = 'json'
    elif splitext(file_path)[1] == '.yaml' or splitext(file_path)[1] == '.yml':
        file_format = 'yaml'
    else:
        raise TypeError('Unknown file type!')
    return open(file_path).read(), file_format


def parse_string(string, string_format):
    if string_format == 'json':
        return json_loads(string)
    elif string_format == 'yaml':
        return yaml_loads(string)
    else:
        raise TypeError('Unknown string format!')


def generate_diff(file_path1, file_path2, style=STYLISH):
    string1 = parse_string(*read_file(file_path1))
    string2 = parse_string(*read_file(file_path2))
    answer = make_inner_diff(string1, string2)
    return form_output(answer, style)
