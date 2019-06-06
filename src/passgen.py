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


class Generator():


    def __init__(self, pool, random_generator, c_min=0, c_max=None):
        self.pool = pool
        self.set_limits(c_min, c_max)
        self.counter = 0
        self.random_generator = random_generator

    def set_limits(self, c_min, c_max):
        self.min = max(0, int(c_min))
        self.max = c_max
        if self.max is not None and self.min > self.max:
            raise Exception("c_min should not be greater than c_max")

    def generate(self):
        try:
            char = self.random_generator.choice(self.pool)
        except:
            char = random.choice(self.pool)
        self.counter += 1
        return char

    def __iter__(self):
        while not self.max_achieved():
            yield self.generate()

    def min_achieved(self):
        return self.counter >= self.min

    def max_achieved(self):
        if self.max is None:
            return False
        return self.counter >= self.max

class SuperGenerator(Generator):


    def __init__(self, random_generator, c_min=0, c_max=None):
        self.set_limits(c_min, c_max)
        self.counter = 0
        self.random_generator = random_generator
        self.generators = []
        self.minimums_achieved = False
        self.maximums_achieved = False

    def generate(self):
        if not self.minimums_achieved:
            pool = [i for i in self.generators if not i.min_achieved()]
            if len(pool) == 0:
                self.minimums_achieved = True
                return self.generate()
        elif not self.maximums_achieved:
            pool = [i for i in self.generators if not i.max_achieved()]
            if len(pool) == 0:
                self.maximums_achieved = True
                raise Exception("All maximums achieved")
        else:
            raise Exception("All maximums achieved")
        try:
            generator = self.random_generator.choice(pool)
        except:
            generator = random.choice(pool)
        char = generator.generate()
        self.counter += 1
        return char

    def add(self, gen):
        self.generators.append(gen)

def passgen(length=12, punctuation=False, digits=True, letters=True,
            case="both", **kwargs):
    """Generate random password.

    Args:
        length (int): The length of the password.  Must be greater than
            zero. Defaults to 12.
        punctuation (bool): Whether to use punctuation or not.  Defaults
            to False.
        limit_punctuation (str): Limits the allowed puncturation to defined 
            characters.
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

    if not case in ("both", "lower", "upper"):
        raise ValueError("case can only be 'both', 'upper' or 'lower'")

    p_min = punctuation
    p_max = 0 if punctuation is False else length
    d_min = digits
    d_max = 0 if digits is False else length
    a_u_min = letters if case in ("both", "upper") else 0
    a_u_max = 0 if letters is False or case == "lower" else length
    a_l_min = letters if case in ("both", "lower") else 0
    a_l_max = 0 if letters is False or case == "upper" else length

    if d_min + p_min + a_u_min + a_l_min > length:
        raise ValueError("Minimum punctuation and digits number cannot be greater than length")    
    if not digits and not letters:
        raise ValueError("digits and letters cannot be False at the same time")
    if length < 1:
        raise ValueError("length must be greater than zero")

    if punctuation:
        limit_punctuation = kwargs.get('limit_punctuation', '')
        if limit_punctuation == '':
            punctuation_set = string.punctuation
        else:
            # In case limit_punctuation contains non-punctuation characters
            punctuation_set = ''.join([p for p in limit_punctuation
                                       if p in string.punctuation])
    else:
        punctuation_set = string.punctuation

    srandom = random.SystemRandom()
    p_generator = Generator(punctuation_set, srandom, p_min, p_max)
    d_generator = Generator(string.digits, srandom, d_min, d_max)
    a_u_generator = Generator(string.ascii_uppercase, srandom, a_u_min, a_u_max)
    a_l_generator = Generator(string.ascii_lowercase, srandom, a_l_min, a_l_max)

    main_generator = SuperGenerator(srandom, length, length)
    main_generator.add(p_generator)
    main_generator.add(a_u_generator)
    main_generator.add(a_l_generator)
    main_generator.add(d_generator)
    chars = []
    for i in main_generator:
        chars.append(i)
    try:
        srandom.shuffle(chars, srandom)
    except:
        random.shuffle(chars)
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
    parser.add_argument("--limit-punctuation",
                        help="specify allowed punctuation characters",
                        action='store', default='')
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
                      limit_punctuation=args.limit_punctuation,
                      digits=args.digits,
                      letters=args.letters, case=case))

if __name__ == "__main__":
    main()
