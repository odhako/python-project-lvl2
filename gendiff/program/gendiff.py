from gendiff.program.diff_maker import make_node, make_leaf
from gendiff.format.output import form_output
from json import loads as json_loads
from yaml import safe_load as yaml_loads


def open_file(file_path):
    if file_path.endswith('.json'):
        file_format = 'json'
    elif file_path.endswith(('.yaml', '.yml')):
        file_format = 'yaml'
    else:
        raise TypeError('Unknown file type!')
    return open(file_path).read(), file_format


def parse_string(string, string_format='json'):
    if string_format == 'json':
        return json_loads(string)
    elif string_format == 'yaml':
        return yaml_loads(string)


def make_inner_diff(file1, file2):  # noqa: C901
    def walk(item1, item2, acc):
        for key, value in item1.items():
            if key in item2 and type(value) == dict == type(item2[key]):  # noqa
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
            if key in item1 and type(value) == dict == type(item1[key]):  # noqa
                pass
            elif key in item1 and value == item1[key]:
                pass
            else:
                status = '+'
                acc.append(make_leaf(key, status, value))
        return acc
    answer = []
    answer = walk(file1, file2, answer)
    return answer


def generate_diff(file_path1, file_path2, style='stylish'):
    file1 = parse_string(*open_file(file_path1))
    file2 = parse_string(*open_file(file_path2))
    answer = make_inner_diff(file1, file2)
    return form_output(answer, style)
