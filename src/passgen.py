#!/usr/bin/env python
"""This module contains tools for random password generation.

The module contains two functions:

    - passgen -- generate random password.
    - main -- the main entry point.
"""
from __future__ import print_function
import string
import random
import argparse
import sys


def passgen(length=12, punctuation=False, digits=True, letters=True,
            case="both"):
    """Generate random password.

    Args:
        length (int): The length of the password.  Must be greater than
            zero. Defaults to 12.
        punctuation (bool): Whether to use punctuation or not.  Defaults
            to False.
        digits (bool): Whether to use digits or not.  Defaults to True.
            One of *digits* and *letters* must be True.
        letters (bool): Whether to use letters or not.  Defaults to
            True. One of *digits* and *letters* must be True.
        case (str): Letter case to use.  Accepts 'upper' for upper case,
            'lower' for lower case, and 'both' for both.  Defaults to
            'both'.

    Returns:
        str. The generated password.

    Raises:
        ValueError

    Below are some basic examples.

    >>> passgen()
    z7GlutdEEbnk

    >>> passgen(case='upper')
    Q81J9DOAMBRN

    >>> passgen(length=6)
    EzJMRX
    """
    if not digits and not letters:
        raise ValueError("digits and letters cannot be False at the same time")
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

    chars = [random.choice(pool) for _ in range(length)]
    return "".join(chars)


def _error(msg=""):
    print("passgen: error: " + msg, file=sys.stderr)
    sys.exit(1)


def main():
    """The main entry point for command line invocation. It's output
    is adjusted by command line arguments. By default it outputs 10
    passwords.

    For help on accepted arguments, run::

        $ passgen -h

    Or::

        $ python -m passgen -h
    """
    parser = argparse.ArgumentParser(
        description="Generate random password."
    )
    parser.add_argument("-l", "--length",
                        help="the length of the generated "
                             "password (default: 12)",
                        type=int, default=12)
    parser.add_argument("-n", "--number",
                        help="how many passwords to generate (default: 10)",
                        type=int, default=10)
    parser.add_argument("-p", "--punctuation",
                        help="use punctuation characters",
                        action='store_true')
    alnum_group = parser.add_mutually_exclusive_group()
    alnum_group.add_argument("--no-digits",
                             help="don't use digits",
                             action='store_false', dest='digits')
    alnum_group.add_argument("--no-letters",
                             help="don't use letters",
                             action='store_false', dest='letters')
    case_group = parser.add_mutually_exclusive_group()
    case_group.add_argument("--upper",
                            help="use only upper case letters",
                            action='store_true')
    case_group.add_argument("--lower",
                            help="use only lower case letters",
                            action='store_true')
    args = parser.parse_args()

    if args.length < 1:
        _error("argument -l/--length must be greater than zero")
    if args.number < 1:
        _error("argument -n/--number must be greater than zero")

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

if __name__ == "__main__":
    main()
