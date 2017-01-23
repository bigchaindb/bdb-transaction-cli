#!/usr/bin/env python

import copy
import json
import pdb
import os
import sys
import unittest
from unittest.mock import patch

import pytest
from bigchaindb.common.exceptions import KeypairMismatchException
from bigchaindb import version
from click.testing import CliRunner

from bdb_transaction_cli import cli


PUB1 = '35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF'
PRIV1 = '3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5'

PUB2 = 'EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15'
PRIV2 = 'HrQWRzMwGfLJHkQsaXMef7beMTV4M5aynK4Xm1roFq5V'


OUTPUT2 = {
    'amount': 1,
    'condition': {
        'details': {
            'bitmask': 32,
            'public_key': PUB2,
            'signature': None,
            'type': 'fulfillment',
            'type_id': 4
        },
        'uri': 'cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96'
    },
    'public_keys': [PUB2]
}

# TODO: remove
OUTPUT2_WITH_ID = copy.copy(OUTPUT2)


ASSET = {
    "id": "b87bcc5e5700807ec64b949e7e6f8bccc269d2c6bc3b302632b366e01bc13507",
    "data": None,
}


TX_CREATE = {
    'id': 'b87bcc5e5700807ec64b949e7e6f8bccc269d2c6bc3b302632b366e01bc13507',
    'outputs': [OUTPUT2_WITH_ID],
    'metadata': None,
    "asset": ASSET,
    'inputs': [
        {
            'fulfillment': {
                'bitmask': 32,
                'public_key': PUB1,
                'signature': None,
                'type': 'fulfillment',
                'type_id': 4
            },
            'fulfills': None,
            'owners_before': [PUB1]
        }
    ],
    'operation': 'CREATE',
    'version': version.__version__
}

INPUT2 = {
    'fulfillment': {
        'bitmask': 32,
        'public_key': PUB2,
        'signature': None,
        'type': 'fulfillment',
        'type_id': 4
    },
    'fulfills': {
        'output': 0,
        'txid': TX_CREATE['id']
    },
    'owners_before': [PUB2]
}


TX_CREATE_SIGNED = {
    'id': 'b87bcc5e5700807ec64b949e7e6f8bccc269d2c6bc3b302632b366e01bc13507',
    'outputs': [OUTPUT2_WITH_ID],
    'metadata': None,
    "asset": ASSET,
    'inputs': [
        {
            'fulfillment': 'cf:4:HvQ3Eg9U6Crw-DFf2v36GaPYsEMLhBSSZEuXNQ6cZFhBkAoActcNJro7brIbUl9tVRl0fDjECF36GhvQaUV_HUm0si2l_Lm9li9dp1tljKqia89vuLTgfFLGfuh2BnIP',  # noqa
            'fulfills': None,
            'owners_before': [PUB1]
        }
    ],
    'operation': 'CREATE',
    'version': version.__version__
}


TX_TRANSFER = {
    "id": "9147d3d33f9a6a5122fc7211d34e463c354eec8bafdeeb2e490cb6a550624f3d",
    "operation": "TRANSFER",
    "outputs": [OUTPUT2],
    "inputs": [INPUT2],
    "asset": {"id": ASSET['id'], "data": None},
    "metadata": None,
    "version": version.__version__,
}


RECORD_EXAMPLES = 'RECORD_EXAMPLES' in os.environ


@patch('bdb_transaction_cli.cli.generate_key_pair', lambda: ('b', 'a'))
class TestBdbCli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if RECORD_EXAMPLES:
            cls.doc = open('docs/examples.rst', 'w')
            cls.doc.write("Invocation Examples\n")
            cls.doc.write("===================\n\n")
            print("These are examples of how to invoke the bdb command, "
                  "auto-generated from the tests.", file=cls.doc)

    def invoke_method(self, args):
        args = [json.dumps(arg) if isinstance(arg, (dict, list))
                else arg for arg in args]
        runner = CliRunner()
        result = runner.invoke(cli.main, args)
        if result.exit_code != 0:
            print(result.output, file=sys.stderr)
            raise result.exception
        if args and RECORD_EXAMPLES:
            self.record(args, result.output)
        return result.output

    def record(self, args, output):
        """
        Here's what's happening.

        As the tests are running, this method is rendering each of the calls
        the command line interface into a .rst document.

        It's ugly and hacky but perhaps useful until hand curated usage
        examples are in place. And it has the benefit that it's correct as long
        as the tests are working.
        """
        import inspect
        test_name = inspect.stack()[2][3][5:]

        print('\n\n' + test_name, file=self.doc)
        print('-' * len(test_name), file=self.doc)
        self.doc.write('\n\n.. code-block:: shell\n\n')

        command = cli.main.commands[args[0]]

        var_args = []
        for param, arg in zip(command.params, args[1:]):
            opt = None
            if arg.startswith('--'):
                opt, arg = arg.split('=', 2)

            if arg[0] in '[{':
                body = json.dumps(json.loads(arg), indent=4, sort_keys=True)
                body = body.replace('\n', '\n   ')
                stmt = "   $ {}='{}'\n\n".format(param.name.upper(), body)
                self.doc.write(stmt)
                arg = "\"${}\"".format(param.name.upper())

            if opt:
                var_args.insert(0, opt + '=' + arg)
            else:
                var_args.append(arg)

        self.doc.write('\n   $ bdb {} {}\n'.format(args[0], ' '.join(var_args)))

    def test_usage(self):
        output = self.invoke_method([])
        assert output.startswith('Usage:')

    def test_create(self):
        output = json.loads(self.invoke_method(['create', PUB1, OUTPUT2]))
        self.assertEqual(output, TX_CREATE)

    def test_create_with_asset(self):
        asset_data = {'b': 1}
        asset_arg = '--asset-data=' + json.dumps(asset_data)
        args = ['create', PUB1, OUTPUT2, asset_arg]
        output = json.loads(self.invoke_method(args))
        self.assertEqual(output['asset']['data'], asset_data)

    def test_generate_output(self):
        output = json.loads(self.invoke_method(['generate_output', PUB2]))
        assert output == OUTPUT2

    def test_spend(self):
        output = json.loads(self.invoke_method(['spend', TX_CREATE]))
        assert output == [INPUT2]

    def test_spend_with_condition_ids(self):
        output = json.loads(self.invoke_method(['spend', TX_CREATE, '[0]']))
        assert output == [INPUT2]

    def test_generate_keys(self):
        output = self.invoke_method(['generate_keys']).rstrip()
        assert json.loads(output) == {'public': 'a', 'private': 'b'}

    def test_generate_keys_with_name(self):
        output = self.invoke_method(['generate_keys', '--name=bob']).rstrip()
        assert output == 'bob_pub=a bob_priv=b'

    def test_sign(self):
        self.maxDiff = None
        output = json.loads(self.invoke_method(['sign', TX_CREATE, PRIV1]))
        self.assertEqual(output, TX_CREATE_SIGNED)

    def test_sign_fails(self):
        with pytest.raises(KeypairMismatchException):
            self.invoke_method(['sign', TX_CREATE, PRIV2])

    def test_transfer(self):
        self.maxDiff = None
        args = ['transfer', [INPUT2], [OUTPUT2], json.dumps(ASSET)]
        output = json.loads(self.invoke_method(args))
        self.assertEqual(output, TX_TRANSFER)

    def test_get_asset(self):
        output = json.loads(self.invoke_method(['get_asset', TX_CREATE]))
        assert output == {'id': ASSET['id']}



# Here we monkey patch pdb to make it work inside click's CliRunner
pdb.set_trace = pdb.Pdb(stdin=sys.stdin, stdout=sys.stdout).set_trace
