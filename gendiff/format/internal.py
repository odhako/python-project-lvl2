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


ADDED = 'ADDED'
REMOVED = 'REMOVED'
CHILDREN = 'CHILDREN'
NOT_CHANGED = 'NOT CHANGED'
