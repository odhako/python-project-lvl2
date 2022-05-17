import json


def start():
    print('Hello, World! This is gendiff.')


def generate_diff(file_path1, file_path2):
    from json import load
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    for x, y in file1.items():
        print(f'{x}: {y}')
    print('--------------------------------')
    for x, y in file2.items():
        print(f'{x}: {y}')
    return


def cli():
    import argparse
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


# generate_diff('../../tests/fixtures/file1.json', '../../tests/fixtures/file2.json')