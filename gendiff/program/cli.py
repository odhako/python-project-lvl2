import argparse
from gendiff import generate_diff  # stylish


def cli():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output', choices=['stylish', ])
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    if args.format == 'stylish':
        pass
        # print(generate_diff(args.first_file, args.second_file, stylish))
    else:
        print(generate_diff(args.first_file, args.second_file))
