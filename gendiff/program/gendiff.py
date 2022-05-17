def check_type(value):
    if type(value) == bool:
        return str(value).lower()
    else:
        return value


def generate_diff(file_path1, file_path2):
    from json import load as json_load
    file1 = json_load(open(file_path1))
    file2 = json_load(open(file_path2))
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


def cli():
    import argparse
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
