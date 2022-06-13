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


def get_key(item):
    return item['key']


def is_node(item):
    return 'children' in item


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
                    acc.append(
                        make_node(
                            key, CHILDREN, walk(item1[key], item2[key], acc=[])
                        )
                    )
                elif item1[key] == item2[key]:
                    acc.append(make_leaf(key, NOT_CHANGED, item1[key]))
                else:
                    acc.append(make_leaf(key, REMOVED, item1[key]))
                    acc.append(make_leaf(key, ADDED, item2[key]))
        return acc

    answer = walk(dict1, dict2)
    return answer
