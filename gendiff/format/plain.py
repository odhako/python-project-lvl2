from gendiff.diff_tree_generator import get_key, get_status, get_value
from gendiff.diff_tree_generator import get_children, ADDED, REMOVED, CHILDREN


def to_string_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    if type(value) == int:
        return value
    encoder = {True: 'true', False: 'false', None: 'null'}
    if value in encoder.keys():
        return encoder[value]
    else:
        return f"'{value}'"


def plain(diff):  # noqa: C901

    def walk(children, acc, path):
        for index, item in enumerate(sorted(children, key=get_key)):
            if get_status(item) == CHILDREN:
                new_path = path + get_key(item) + '.'
                walk(get_children(item), acc, new_path)
            else:
                if get_status(item) == REMOVED:
                    if index == len(children) - 1:
                        acc.append(
                            f"Property '{path + get_key(item)}' was removed"
                        )
                    else:
                        next_key = get_key(
                            sorted(children, key=get_key)[index + 1]
                        )
                        if get_key(item) == next_key:
                            next_value = get_value(
                                sorted(children, key=get_key)[index + 1]
                            )
                            acc.append(
                                f"Property '{path + get_key(item)}' "
                                f"was updated. From "
                                f"{to_string_plain(get_value(item))} to "
                                f"{to_string_plain(next_value)}"
                            )
                        else:
                            acc.append(
                                f"Property '{path + get_key(item)}' was removed"
                            )
                elif get_status(item) == ADDED:
                    if get_key(item) == \
                            get_key(sorted(children, key=get_key)[index - 1]):
                        pass
                    else:
                        acc.append(
                            f"Property '{path + get_key(item)}' "
                            f"was added with value: "
                            f"{to_string_plain(get_value(item))}"
                        )
        return acc

    result = walk(diff, [], '')
    result = '\n'.join(result)
    return result
