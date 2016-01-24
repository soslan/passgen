passgen
=======

passgen is a tool for generating random passwords. It provides both
command line utility and underlying python module.

Installation
============

passgen requires Python 2.7 or 3.x.

passgen can be installed with `pip`::

    $ pip install passgen

To install it from source, enter the source distribution directory and run::

    $ python setup.py install

To install in development mode, run from project directory::

    $ pip install --user -e .

Usage (command line)
====================

The most basic usage of passgen command line utility prints 10 random
passwords, and is as follows::

    $ passgen

passgen accepts several arguments configuring its outcome.
Overall synopsis is::

    $ passgen [-h] [-l LENGTH] [-n NUMBER] [-p] [--no-digits | --no-letters]
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

Below are some examples of passgen usage.

Output one password::

    $ passgen -n 1
    faFMKqApw24P

Generate one password with eight characters::

    $ passgen -n 1 -l 8
    h2MowzBQ

Generate one password with all upper case letters::

    $ passgen -n 1 --upper
    3TLJ73WQSG6U

Generate one password with punctuation characters::

    $ passgen -n 1 -p
    oFmCF|s8kCE~

Python module
=============

passgen Python module provides just one function also called passgen.

| ``passgen(length=12, punctuation=False, digits=True, letters=True,
            case='both')``

It returns a random string with *length* characters. *punctuation*, *digits*
and *letters* arguments specify whether punctuation, digits and letters
should be used. *case* specifies letter case and can be one of 'upper',
'lower' or 'both'.

For more details, run::

    $ python -c 'import passgen; help(passgen.passgen)'

Testing
=======

The passgen tests are done using ``unittest``. For running the tests, run from
project directory::

    $ python tests/test_passgen.py -v

TODO
====

- Implement generation from format string.
  For example, 'ddd' generating three-digit password.

- Allow occurance restrictions on punctuation, digits and letters.
  For example, ``passgen(min-punctuation=1)`` returning password with at least
  one punctuation.

License
=======

See LICENSE.
