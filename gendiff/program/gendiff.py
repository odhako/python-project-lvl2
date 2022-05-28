from gendiff.format.internal import check_in, make_node, make_leaf
from gendiff.format.stylish import stylish


def load_file(file_path):
    if file_path.endswith('.json'):
        from json import load as file_load
    elif file_path.endswith(('.yaml', '.yml')):
        from yaml import safe_load as file_load
    else:
        raise TypeError('Unknown file type!')
    return file_load(open(file_path))


def generate_diff(file_path1, file_path2, style=stylish):  # noqa: C901
    file1 = load_file(file_path1)
    file2 = load_file(file_path2)

    def walk(item1, item2, acc):
        for key, value in item1.items():
            if key in item2 and type(value) == dict == type(item2[key]):  # noqa
                status = ' '
                acc.append(
                    make_node(key, status, walk(value, item2[key], acc=[])))  # noqa
            elif key in item2 and value == item2[key]:
                status = ' '
                acc.append(make_leaf(key, status, check_in(value)))
            else:
                status = '-'
                acc.append(make_leaf(key, status, check_in(value)))
        for key, value in item2.items():
            if key in item1 and type(value) == dict == type(item1[key]):  # noqa
                pass
            elif key in item1 and value == item1[key]:
                pass
            else:
                status = '+'
                acc.append(make_leaf(key, status, check_in(value)))
        return acc

    answer = []
    answer = walk(file1, file2, answer)
    return style(answer)
