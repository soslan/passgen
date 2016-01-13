import string
import random
import argparse


def passgen(length=12):
    """Generate a strong password with *length* characters"""
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.SystemRandom().choice(pool) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(
        description="Generate strong random password."
    )
    parser.add_argument("-l", "--length",
                        help="the number of characters to generate "
                             "for each password",
                        type=int, default=12)
    parser.add_argument("-n", "--number",
                        help="how many passwords to generate",
                        type=int, default=10)

    args = parser.parse_args()
    for _ in range(args.number):
        print passgen(args.length)
