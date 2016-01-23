passgen
=======

passgen is a tool for generating random passwords. It provides both
command line utility and underlying python module.

Installation
============

passgen can be installed with pip::

    $ pip install passgen

Usage (command line)
====================

Basic usage of passgen command line utility is as follows::

    $ passgen

passgen can also accepts several arguments configuring the outcome.
Overall synopsis is::

    $ passgen [-h] [-l LENGTH] [-n NUMBER] [-p] [--no-digits] [--no-letters]
              [--upper | --lower]

Arguments:

-h
    Display help

-l, --length LENGTH
    Passwords should contain LENGTH characters. Defaults to 12.

-n, --number NUMBER
    Generate NUMBER passwords. Defaults to 10.

-p, --punctuation
    Use punctuation characters

--no-digits
    Don't use digits

--no-letters
    Don't use letters

--upper
    Use only upper case letters

--lower
    Use only lower case letters

Examples
--------

Below are some examples of passgen usage::

    # Most basic usage. Outputs 10 passwords.
    $ passgen

    # Using -n argument. Generate just two passwords.
    $ passgen -n 2

    # Using -l argument. Generate passwords with eight characters.
    $ passgen -l 8

Python module
=============

passgen Python module provides just one function also called passgen.

passgen(length=12, punctuation=False, digits=True, letters=True, case='both')
    Returns a random string with *length* characters. *punctuation*, *digits*
    and *letters* arguments specify whether punctuation, digits and letters
    should be used. *case* specifies letter case and can be one of 'upper',
    'lower' or 'both'.

For more details, run::

    $ python -c 'import passgen; help(passgen.passgen)'

TODO
====

- Implement generation from format string.
  For example, 'ddd' generating three-digit password.

License
=======

See LICENSE.
