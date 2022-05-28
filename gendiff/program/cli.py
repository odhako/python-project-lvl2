import argparse
from gendiff import generate_diff, plain


def cli():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output',
                        choices=['stylish', 'plain'])
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, plain))
    else:
        print(generate_diff(args.first_file, args.second_file))
