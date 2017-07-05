#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'bigchaindb~=1.0.0',
]

dev_requirements = [
    'pip==8.1.2',
    'bumpversion==0.5.3',
    'wheel==0.29.0',
    'watchdog==0.8.3',
    'flake8==2.6.0',
    'tox==2.3.1',
    'coverage==4.1',
    'Sphinx==1.4.8',
    'cryptography==1.4',
    'PyYAML==3.11',
    'pytest==2.9.2',
    'ipdb',
    'graphviz'
]

test_requirements = [
]

setup(
    name='bdb_transaction_cli',
    version='0.1.0',
    description=("A minimal command line tool for creating and signing "
                 "BigchainDB transactions."),
    long_description=readme + '\n\n' + history,
    author="BigchainDB GmbH",
    author_email='dev@bigchaindb.com',
    url='https://github.com/bigchaindb/bdb-transaction-cli',
    packages=['bdb_transaction_cli'],
    package_dir={'bdb_transaction_cli': 'bdb_transaction_cli'},
    entry_points={
        'console_scripts': [
            'bdb=bdb_transaction_cli.__main__:main'
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
