#!/usr/bin/env python3
import argparse
import os


def main(args):
    print(f"num_a: {args.num_a}")
    print(f"num_b: {args.num_b}")
    print(f"sum: {args.num_a + args.num_b}")

    secret = os.getenv('SECRET_VALUE')
    print(f"\nsecret value: {secret}")


def parse_arguments():
    desc = "Simple script"
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--num_a', required=True, type=float, help='Number 1')
    parser.add_argument('--num_b', required=True, type=float, help='Number 2')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
