from gendiff.format.output import form_output, STYLISH
from json import loads as json_loads
from yaml import safe_load as yaml_loads


def read_file(file_path):
    if file_path.endswith('.json'):
        file_format = 'json'
    elif file_path.endswith(('.yaml', '.yml')):
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


def make_node(key, status, children):
    node = {
        'key': key,
        'status': status,
        'children': children
    }
    return node


def make_leaf(key, status, value):
    leaf = {
        'key': key,
        'status': status,
        'value': value
    }
    return leaf


def make_inner_diff(dict1, dict2):  # noqa: C901
    def walk(item1, item2, acc=[]):
        for key, value in item1.items():
            if key in item2 and type(value) == dict and type(item2[key]) == dict: # noqa
                status = ' '
                acc.append(
                    make_node(
                        key, status, walk(value, item2[key], acc=[])
                    )
                )
            elif key in item2 and value == item2[key]:
                status = ' '
                acc.append(make_leaf(key, status, value))
            else:
                status = '-'
                acc.append(make_leaf(key, status, value))
        for key, value in item2.items():
            if key in item1 and type(value) == dict and type(item1[key]) == dict:  # noqa
                pass
            elif key in item1 and value == item1[key]:
                pass
            else:
                status = '+'
                acc.append(make_leaf(key, status, value))
        return acc
    answer = walk(dict1, dict2)
    return answer


def generate_diff(file_path1, file_path2, style=STYLISH):
    file1 = parse_string(*read_file(file_path1))
    file2 = parse_string(*read_file(file_path2))
    answer = make_inner_diff(file1, file2)
    return form_output(answer, style)
