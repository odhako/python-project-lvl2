import argparse
from gendiff import stylish


def cli(generate_diff):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(stylish(generate_diff(args.first_file, args.second_file)))
