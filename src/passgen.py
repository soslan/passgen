#!/usr/bin/env python
from __future__ import print_function
import string
import random
import argparse
import sys


def passgen(length=12, punctuation=False, digits=True, letters=True,
            case="both"):
    """Generate a random password with *length* characters"""
    if length < 1:
        raise ValueError("length must be greater than zero")
    pool = []
    if letters:
        if case == "both":
            pool.append(string.ascii_uppercase + string.ascii_lowercase)
        elif case == "upper":
            pool.append(string.ascii_uppercase)
        elif case == "lower":
            pool.append(string.ascii_lowercase)
        else:
            raise ValueError("case can only be 'both', 'upper' or 'lower'")
    if digits:
        pool.append(string.digits)
    if punctuation:
        pool.append(string.punctuation)
    pool = "".join(pool)

    # Using technique from Stack Overflow answer
    # http://stackoverflow.com/a/23728630
    chars = [random.SystemRandom().choice(pool) for _ in range(length)]
    return "".join(chars)


def _error(msg=""):
    print("passgen: error: " + msg, file=sys.stderr)
    sys.exit(1)


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
    parser.add_argument("--upper",
                        help="use only upper case letters",
                        action='store_true')
    parser.add_argument("--lower",
                        help="use only lower case letters",
                        action='store_true')
    args = parser.parse_args()
    print(args)

    if args.lower and args.upper:
        # --lower and --upper should not be combined
        # sys.stderr.write("passgen: error: --lower and --upper can "
        #                  "not be combined.")
        _error("--lower and --upper can not be combined.")
    if args.lower:
        case = "lower"
    elif args.upper:
        case = "upper"
    else:
        case = "both"

    for _ in range(args.number):
        print(passgen(args.length, punctuation=args.punctuation,
                      digits=args.digits,
                      letters=args.letters, case=case))
