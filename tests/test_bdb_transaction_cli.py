#!/usr/bin/env python

import json
import pdb
import os
import sys
import unittest
from unittest.mock import patch

import pytest
from bigchaindb.common.transaction import Transaction
from bigchaindb.common.exceptions import KeypairMismatchException
from click.testing import CliRunner

from bdb_transaction_cli import cli


PUB1 = '35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF'
PRIV1 = '3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5'

PUB2 = 'EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15'
PRIV2 = 'HrQWRzMwGfLJHkQsaXMef7beMTV4M5aynK4Xm1roFq5V'


OUTPUT2 = {
    'amount': '1',
    'condition': {
        'details': {
            'public_key': PUB2,
            'type': 'ed25519-sha-256',
        },
        'uri': 'ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072'
    },
    'public_keys': [PUB2]
}


ASSET = {
    'data': None,
}


TX_CREATE = {
    'id': 'f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0',
    'outputs': [OUTPUT2],
    'metadata': None,
    'asset': ASSET,
    'inputs': [
        {
            'fulfillment': {
                'public_key': PUB1,
                'type': 'ed25519-sha-256',
            },
            'fulfills': None,
            'owners_before': [PUB1]
        }
    ],
    'operation': 'CREATE',
    'version': Transaction.VERSION,
}

INPUT2 = {
    'fulfillment': {
        'public_key': PUB2,
        'type': 'ed25519-sha-256',
    },
    'fulfills': {
        'output_index': 0,
        'transaction_id': TX_CREATE['id']
    },
    'owners_before': [PUB2]
}


TX_CREATE_SIGNED = {
    'id': 'f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0',
    'outputs': [OUTPUT2],
    'metadata': None,
    'asset': ASSET,
    'inputs': [
        {
            'fulfillment': 'pGSAIB70NxIPVOgq8PgxX9r9-hmj2LBDC4QUkmRLlzUOnGRYgUC6sct6F5fdDATwbhn4YOPilNNyRcyQiqH-f9tNnqxMemwPAW_Wcd7ej7znQQa58IAVFHSFuYdWNktBOypumW4O',  # noqa
            'fulfills': None,
            'owners_before': [PUB1]
        }
    ],
    'operation': 'CREATE',
    'version': Transaction.VERSION,
}


TX_TRANSFER = {
    'id': 'e52b682a508a8268fd5b3af5dd8a81fa04c6edcadfff5068a267222c5b1dc5cc',
    'operation': 'TRANSFER',
    'outputs': [OUTPUT2],
    'inputs': [INPUT2],
    'asset': {'id': TX_CREATE['id']},
    'metadata': None,
    'version': Transaction.VERSION,
}


RECORD_EXAMPLES = 'RECORD_EXAMPLES' in os.environ


@patch('bdb_transaction_cli.cli.generate_key_pair', lambda: ('b', 'a'))
class TestBdbCli(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
    @classmethod
    def setUpClass(cls):
        if RECORD_EXAMPLES:
            cls.doc = open('docs/examples.rst', 'w')
            cls.doc.write('Invocation Examples\n')
            cls.doc.write('===================\n\n')
            print('These are examples of how to invoke the bdb command, '
                  'auto-generated from the tests.', file=cls.doc)

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
                arg = '"${}"'.format(param.name.upper())

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
        self.assertEqual(TX_CREATE, output)

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
        output = json.loads(self.invoke_method(['sign', TX_CREATE, PRIV1]))

        self.assertEqual(TX_CREATE_SIGNED, output)

    def test_sign_fails(self):
        with pytest.raises(KeypairMismatchException):
            self.invoke_method(['sign', TX_CREATE, PRIV2])

    def test_transfer(self):
        asset = json.loads(self.invoke_method(['get_asset', TX_CREATE]))
        args = ['transfer', [INPUT2], [OUTPUT2], json.dumps(asset)]
        output = json.loads(self.invoke_method(args))
        self.assertEqual(TX_TRANSFER, output)

    def test_get_asset(self):
        output = json.loads(self.invoke_method(['get_asset', TX_CREATE]))
        assert output == {'id': TX_CREATE['id']}



# Here we monkey patch pdb to make it work inside click's CliRunner
pdb.set_trace = pdb.Pdb(stdin=sys.stdin, stdout=sys.stdout).set_trace
