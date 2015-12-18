#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='passgen',
      version='0.0.1',
      author='Soslan Khubulov',
      author_email='soslanx@gmail.com',
      package_dir={'': 'src'},
      entry_points={
          'console_scripts': [
              'passgen = passgen:passgen',
          ],
      },
      py_modules=['passgen'],
      )
