import argparse
from gendiff import generate_diff
from gendiff.format.output import STYLISH, PLAIN, JSON


def cli():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output',
                        choices=[STYLISH, PLAIN, JSON],
                        default=STYLISH)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return generate_diff(args.first_file, args.second_file, args.format)
