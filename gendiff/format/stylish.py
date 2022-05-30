from gendiff.format.internal import is_node, get_key, get_status, get_value
from gendiff.format.internal import get_children, check_stylish


def stylish(diff):  # noqa: C901

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
                acc += f'{indent * depth}  {get_status(item)} ' \
                       f'{get_key(item)}: ' + '{\n'
                depth += 1
                acc += walk(get_children(item), '', depth)
                acc += f'{indent * depth}' + '}\n'
                depth -= 1
            else:
                if isinstance(get_value(item), dict):
                    acc += f'{indent * depth}  {get_status(item)} ' \
                           f'{get_key(item)}: ' + '{\n'
                    depth += 1
                    acc += walk_dict(get_value(item), '', depth)
                    acc += f'{indent * depth}' + '}\n'
                    depth -= 1
                else:
                    acc += f'{indent * depth}  {get_status(item)} ' \
                           f'{get_key(item)}: ' \
                           f'{check_stylish(get_value(item))}\n'
        return acc

    indent = '    '
    output_string = '{\n'
    output_string = walk(diff, output_string, depth=0)
    output_string += '}'
    return output_string
