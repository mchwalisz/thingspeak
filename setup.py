# -*- coding: utf-8 -*-
"""
Client library for the thingspeak.com API

Installation script
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'thingspeak', '__init__.py'), 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='thingspeak',
    version=version,
    description='Client library for the thingspeak.com API',
    long_description=long_description,
    url='https://github.com/mchwalisz/thingspeak',

    author='Mikołaj Chwalisz',
    author_email='m.chwalisz@gmail.com',
    license='LGPLv3',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: ' +
        'GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
    ],
    keywords='thingspeak development api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests', 'docopt'],

    extras_require={
        'dev': ['check-manifest', 'tox', 'sphinx', 'sphinx_bootstrap_theme'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'thingspeak=thingspeak.cmdline:main',
        ],
    },
    include_package_data=True,
)
