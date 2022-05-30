from json import dumps as json_dumps
from gendiff.format.internal import is_node, get_key, get_value
from gendiff.format.internal import get_status, get_children


def json_format(diff):

    def walk_dict(item, acc):
        for key, value in item.items():
            if isinstance(value, dict):
                acc.update({f'  {key}': walk_dict(value, {})})
            else:
                acc.update({f'  {key}': value})
        return acc

    def walk(children, acc):
        for item in sorted(children, key=get_key):
            if is_node(item):
                acc.update({f'{get_status(item)} '
                            f'{get_key(item)}': walk(get_children(item), {})})
            else:
                if isinstance(get_value(item), dict):
                    acc.update({f'{get_status(item)} '
                                f'{get_key(item)}':
                                    walk_dict(get_value(item), {})})
                else:
                    acc.update({f'{get_status(item)} '
                                f'{get_key(item)}': get_value(item)})
        return acc

    result = {}
    result = walk(diff, result)
    return json_dumps(result)
