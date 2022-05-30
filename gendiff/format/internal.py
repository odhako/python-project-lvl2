def check_stylish(value):
    encoder = {True: 'true', False: 'false', None: 'null'}
    if value in encoder.keys():
        return encoder[value]
    else:
        return value


def check_plain(value):
    encoder = {True: 'true', False: 'false', None: 'null'}
    if isinstance(value, dict):
        return "[complex value]"
    elif value in encoder.keys():
        return encoder[value]
    else:
        return f"'{value}'"


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
