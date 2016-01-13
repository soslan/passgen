import string
import random
import argparse


def passgen(length=8):
    """Generate a strong password with *length* characters"""
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.SystemRandom().choice(pool) for _ in range(length))


def main():
    parser = argparse.ArgumentParser("Generate strong random password.")
    parser.add_argument("length",
                        help="the number of characters to generate",
                        type=int)
    parser.add_argument("-n", "--number",
                        help="how many passwords to generate",
                        type=int)

    args = parser.parse_args()
    for _ in range(args.number):
        print passgen(args.length)
