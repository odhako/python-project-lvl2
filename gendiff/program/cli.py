import argparse
from gendiff import generate_diff, plain, json_format


def cli():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output',
                        choices=['stylish', 'plain', 'json'])
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, plain))
    elif args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, json_format))
    else:
        print(generate_diff(args.first_file, args.second_file))
