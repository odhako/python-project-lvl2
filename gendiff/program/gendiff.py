def check_type(value):
    if type(value) == bool:
        return str(value).lower()
    else:
        return value


def load_file(file_path):
    if file_path.endswith('.json'):
        from json import load as file_load
    elif file_path.endswith(('.yaml', '.yml')):
        from yaml import safe_load as file_load
    else:
        raise TypeError('Unknown file type!')
    return file_load(open(file_path))


def generate_diff(file_path1, file_path2):
    file1 = load_file(file_path1)
    file2 = load_file(file_path2)
    result = {}
    for key, value in file1.items():
        if key in file2 and value == file2[key]:
            result.setdefault(key, {}).update({' ': check_type(value)})
        else:
            result.setdefault(key, {}).update({'-': check_type(value)})
    for key, value in file2.items():
        if key in file1 and value == file1[key]:
            pass
        else:
            result.setdefault(key, {}).update({'+': check_type(value)})
    string_out = '{\n'
    for key, value in sorted(result.items()):
        if ' ' in value.keys():
            string_out += f'    {key}: {value[" "]}\n'
        else:
            if '-' in value.keys():
                string_out += f'  - {key}: {value["-"]}\n'
            if '+' in value.keys():
                string_out += f'  + {key}: {value["+"]}\n'
    string_out += '}'
    return string_out
