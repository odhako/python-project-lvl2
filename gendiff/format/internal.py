def check_in(value):
    if type(value) == bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def check_out(value):
    if value in ['true', 'false', 'null']:
        return value
    elif isinstance(value, dict):
        return "[complex value]"
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
