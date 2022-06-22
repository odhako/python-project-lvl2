from gendiff.diff_tree_generator import is_node, get_key, get_status, get_value
from gendiff.diff_tree_generator import get_children, ADDED, REMOVED, CHILDREN
from gendiff.diff_tree_generator import NOT_CHANGED


def get_output_status(status):
    return {ADDED: '+', REMOVED: '-', CHILDREN: ' ', NOT_CHANGED: ' '}[status]


def to_string_stylish(value):
    if type(value) == int:
        return value
    encoder = {True: 'true', False: 'false', None: 'null'}
    if value in encoder.keys():
        return encoder[value]
    return value


def stylish(diff):  # noqa: C901

    def walk_dict(item, acc, depth):
        for key, value in sorted(item.items()):
            if isinstance(value, dict):
                acc.append(f'{indent * depth}    {key}: ' + '{')
                depth += 1
                acc.extend(walk_dict(value, [], depth))
                acc.append(f'{indent * depth}' + '}')
                depth -= 1
            else:
                acc.append(f'{indent * depth}    {key}: {value}')
        return acc

    def walk(children, acc, depth):
        for item in sorted(children, key=get_key):
            if is_node(item):
                acc.append(
                    f'{indent * depth}  {get_output_status(get_status(item))} '
                    f'{get_key(item)}: ' + '{'
                )
                depth += 1
                acc.extend(walk(get_children(item), [], depth))
                acc.append(f'{indent * depth}' + '}')
                depth -= 1
            else:
                if isinstance(get_value(item), dict):
                    acc.append(
                        f'{indent * depth}  '
                        f'{get_output_status(get_status(item))} '
                        f'{get_key(item)}: ' + '{'
                    )
                    depth += 1
                    acc.extend(walk_dict(get_value(item), [], depth))
                    acc.append(f'{indent * depth}' + '}')
                    depth -= 1
                else:
                    acc.append(
                        f'{indent * depth}  '
                        f'{get_output_status(get_status(item))} '
                        f'{get_key(item)}: {to_string_stylish(get_value(item))}'
                    )
        return acc

    indent = '    '
    result = walk(diff, ['{'], depth=0)
    result.append('}')
    return '\n'.join(result)
