#!/usr/bin/env python

from setuptools import setup

from googleplaces import __author__, __email__, __version__

DESCRIPTION = 'A simple wrapper around the Google Places API.'

setup(
    name = 'python-google-places',
    version = __version__,
    url = 'http://github.com/url84t/python-google-places',
    author = __author__,
    author_email = __email__,
    packages=['googleplaces'],
    install_requires=[
        'six',
    ],
    description = DESCRIPTION,
)
