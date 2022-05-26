def check_type(value):
    if type(value) == bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def load_file(file_path):
    if file_path.endswith('.json'):
        from json import load as file_load
    elif file_path.endswith(('.yaml', '.yml')):
        from yaml import safe_load as file_load
    else:
        raise TypeError('Unknown file type!')
    return file_load(open(file_path))


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


def is_node(item):
    return 'children' in item


def get_key(item):
    return item['key']


def get_status(item):
    return item['status']


def get_value(item):
    return item['value']


def get_children(item):
    return item['children']


def generate_diff(file_path1, file_path2):
    file1 = load_file(file_path1)
    file2 = load_file(file_path2)

    def walk(item1, item2, acc):
        for key, value in item1.items():
            if key in item2 and type(value) == dict == type(item2[key]):
                status = ' '
                acc.append(make_node(key, status, walk(value, item2[key], acc=[])))
            elif key in item2 and value == item2[key]:
                status = ' '
                acc.append(make_leaf(key, status, check_type(value)))
            else:
                status = '-'
                acc.append(make_leaf(key, status, check_type(value)))
        for key, value in item2.items():
            if key in item1 and type(value) == dict == type(item1[key]):
                pass
            elif key in item1 and value == item1[key]:
                pass
            else:
                status = '+'
                acc.append(make_leaf(key, status, check_type(value)))
        return acc

    answer = []
    answer = walk(file1, file2, answer)
    return answer


def stylish(diff):

    def walk_dict(item, acc, depth):
        for key, value in sorted(item.items()):
            if isinstance(value, dict):
                acc += f'{indent * depth}    {key}: ' + '{\n'
                depth += 1
                acc += walk_dict(value, '', depth)
                acc += f'{indent * depth}' + '}\n'
                depth -= 1
            else:
                acc += f'{indent * depth}    {key}: {value}\n'
        return acc

    def walk(children, acc, depth):
        for item in sorted(children, key=get_key):
            if is_node(item):
                acc += f'{indent * depth}  {get_status(item)} {get_key(item)}: ' + '{\n'
                depth += 1
                acc += walk(get_children(item), '', depth)
                acc += f'{indent * depth}' + '}\n'
                depth -= 1
            else:
                if isinstance(get_value(item), dict):
                    acc += f'{indent * depth}  {get_status(item)} {get_key(item)}: ' + '{\n'
                    depth += 1
                    acc += walk_dict(get_value(item), '', depth)
                    acc += f'{indent * depth}' + '}\n'
                    depth -= 1
                else:
                    acc += f'{indent * depth}  {get_status(item)} {get_key(item)}: {get_value(item)}\n'
        return acc

    indent = '    '
    output_string = '{\n'
    output_string = walk(diff, output_string, depth=0)
    output_string += '}'
    return output_string
