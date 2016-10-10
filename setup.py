#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'bigchaindb-common>=0.0.3',
]

dev_requirements = [
    'ipdb',
]

test_requirements = [
]

setup(
    name='bdb_transaction_cli',
    version='0.1.0',
    description="A minimal command line tool for create and sign BigchainDB transactions.",
    long_description=readme + '\n\n' + history,
    author="BigchainDB GmbH",
    author_email='dev@bigchaindb.com',
    url='https://github.com/wrigley/bdb_transaction_cli',
    packages=[
        'bdb_transaction_cli',
    ],
    package_dir={'bdb_transaction_cli':
                 'bdb_transaction_cli'},
    entry_points={
        'console_scripts': [
            'bdb_transaction_cli=bdb_transaction_cli.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='bdb_transaction_cli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements
    },
)
