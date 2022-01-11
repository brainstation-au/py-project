import argparse
import os

from package_a.summation import sum_int

def main():
    parser = argparse.ArgumentParser(description='Sum two integers')
    parser.add_argument(
        '--value-a',
        help='Value of a',
        default=os.environ.get('VALUE_A', None),
        required=True)
    parser.add_argument(
        '--value-b',
        help='Value of b',
        default=os.environ.get('VALUE_B', None),
        required=True)

    args = parser.parse_args()
    print(sum_int(int(args.value_a), int(args.value_b)))
