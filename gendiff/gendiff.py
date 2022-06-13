from gendiff.format.internal import ADDED, REMOVED, SAME
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
        keys = set()
        keys.update(item1.keys(), item2.keys())
        for key in keys:
            if key in item1 and key not in item2:
                acc.append(make_leaf(key, REMOVED, item1[key]))
            elif key in item2 and key not in item1:
                acc.append(make_leaf(key, ADDED, item2[key]))
            elif key in item1 and key in item2:
                if type(item1[key]) == dict and type(item2[key]) == dict:
                    status = SAME  # TODO: make new status 'HAS_CHILDREN' for example
                    acc.append(
                        make_node(
                            key, status, walk(item1[key], item2[key], acc=[])
                        )
                    )
                elif item1[key] == item2[key]:
                    acc.append(make_leaf(key, SAME, item1[key]))
                else:
                    acc.append(make_leaf(key, REMOVED, item1[key]))
                    acc.append(make_leaf(key, ADDED, item2[key]))
        return acc

    answer = walk(dict1, dict2)
    return answer


def generate_diff(file_path1, file_path2, style=STYLISH):
    string1 = parse_string(*read_file(file_path1))
    string2 = parse_string(*read_file(file_path2))
    answer = make_inner_diff(string1, string2)
    return form_output(answer, style)
