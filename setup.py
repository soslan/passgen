#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='passgen',
      version='0.1.0',
      description='Strong password generator',
      url='https://github.com/soslan/passgen',
      author='Soslan Khubulov',
      author_email='soslanx@gmail.com',
      license='MIT',
      package_dir={'': 'src'},
      entry_points={
          'console_scripts': [
              'passgen = passgen:main',
          ],
      },
      py_modules=['passgen'],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='password',
      )
