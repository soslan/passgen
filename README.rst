passgen
=======

passgen is a tool for generating strong passwords. It provides both
command line utility and python module.

Installation
============

passgen can be installed with pip:

.. code-block:: bash

    $ pip install passgen

Usage
=====

Basic usage of passgen command line utility is as follows:

.. code-block:: bash

    $ passgen

passgen can also accepts several arguments configuring the outcome.
Overall synopsis is:

.. code-block:: bash

    $ passgen [-h] [-l LENGTH] [-n NUMBER] [-p] [--no-digits] [--no-letters]
              [--upper] [--lower]

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

Below are some examples of passgen usage:

.. code-block:: bash

    # Most basic usage. Outputs 10 passwords.
    $ passgen

    # Using -n argument. Generate just two passwords.
    $ passgen -n 2

    # Using -l argument. Generate passwords with eight characters.
    $ passgen -l 8

TODO
====

- Implement generation from format string.
  For example, 'ddd' generating three-digit password.

License
=======

See LICENSE.
