Changelog
=========

1.1.1 - 2019-06-06

- Fix passgen(case='both') not always including both cases.

1.1.0 - 2018-12-04
------------------

- Add option to limit punctuation.
- Use random.SystemRandom() for more security.
- Introduce Generator and SuperGenerator classes for development flexibility.
- Fix StopIteration error in Python 3.7