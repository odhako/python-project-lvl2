from gendiff.format.internal import check_plain, is_node, get_key, get_status
from gendiff.format.internal import get_value, get_children


def plain(diff):  # noqa: C901

    def walk(children, acc, path):
        for index, item in enumerate(sorted(children, key=get_key)):
            if get_status(item) == ' ':
                if is_node(item):
                    new_path = path + get_key(item) + '.'
                    walk(get_children(item), acc, new_path)
                else:
                    pass
            else:
                if get_status(item) == '-':
                    next_key = get_key(sorted(children, key=get_key)[index + 1])
                    if get_key(item) == next_key:
                        next_value = \
                            get_value(sorted(children, key=get_key)[index + 1])
                        acc.append(
                            f"Property '{path + get_key(item)}' was updated. "
                            f"From {check_plain(get_value(item))} to "
                            f"{check_plain(next_value)}"
                        )
                    else:
                        acc.append(
                            f"Property '{path + get_key(item)}' was removed"
                        )
                elif get_status(item) == '+':
                    if get_key(item) == \
                            get_key(sorted(children, key=get_key)[index - 1]):
                        pass
                    else:
                        acc.append(
                            f"Property '{path + get_key(item)}' "
                            f"was added with value: "
                            f"{check_plain(get_value(item))}"
                        )
        return acc

    result = walk(diff, [], '')
    result = '\n'.join(result)
    return result
