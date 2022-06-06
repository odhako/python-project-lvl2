def check_stylish(value):
    encoder = {True: 'true', False: 'false', None: 'null'}
    for key, key_value in encoder.items():
        if value is key:
            return key_value
        else:
            pass
    return value


def check_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    encoder = {True: 'true', False: 'false', None: 'null'}
    for key, key_value in encoder.items():
        if value is key:
            return key_value
        else:
            pass
    if type(value) == int:
        return value
    else:
        return f"'{value}'"


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
