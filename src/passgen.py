import string
import random
import argparse


def passgen(length=12, punctuation=False, digits=True):
    """Generate a strong password with *length* characters"""
    pool = string.ascii_uppercase + string.ascii_lowercase
    if digits:
        pool = pool + string.digits
    if punctuation:
        pool = pool + string.punctuation

    # Using technique from Stack Overflow answer
    # http://stackoverflow.com/a/23728630
    chars = [random.SystemRandom().choice(pool) for _ in range(length)]
    return "".join(chars)


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
    parser.add_argument("-p", "--punctuation",
                        help="use punctuation characters",
                        action='store_true')
    parser.add_argument("--no-digits",
                        help="don't include digits",
                        action='store_false', dest='digits')
    args = parser.parse_args()
    print args
    for _ in range(args.number):
        print passgen(args.length, punctuation=args.punctuation,
                      digits=args.digits)
