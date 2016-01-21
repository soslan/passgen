import string
import random
import argparse


def passgen(length=12, punctuation=False, digits=True, letters=True):
    """Generate a strong password with *length* characters"""
    pool = []
    if letters:
        pool.append(string.ascii_uppercase + string.ascii_lowercase)
    if digits:
        pool.append(string.digits)
    if punctuation:
        pool.append(string.punctuation)
    pool = "".join(pool)

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
    parser.add_argument("--no-letters",
                        help="don't include letters",
                        action='store_false', dest='letters')
    args = parser.parse_args()
    print(args)

    for _ in range(args.number):
        print(passgen(args.length, punctuation=args.punctuation,
                      digits=args.digits,
                      letters=args.letters))
