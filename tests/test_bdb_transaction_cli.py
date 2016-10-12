#!/usr/bin/env python

import json
import pdb
import sys
from unittest.mock import patch

from click.testing import CliRunner

from bdb_transaction_cli import cli


PUB1 = '35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF'
PRIV1 = '3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5'

PUB2 = 'EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15'
PRIV2 = 'HrQWRzMwGfLJHkQsaXMef7beMTV4M5aynK4Xm1roFq5V'


def invoke_cli(args):
    runner = CliRunner()
    result = runner.invoke(cli.main, args)
    if result.exit_code != 0:
        print(result.output, file=sys.stderr)
    assert result.exit_code == 0
    return result.output


def test_command_line_interface():
    output = invoke_cli([])
    assert output.startswith('Usage:')


COND2 = {
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
    'owners_after': [PUB2]
}


TX1 = {
    'id': '346c094c0c71b51100ad36fcd750d8b3a421a2140fed7e2328c9fba3890f92c0',
    'transaction': {
        'conditions': [
            {'cid': 0, 'condition': COND2['condition'], 'owners_after': [PUB2]}
        ],
        'data': None,
        'fulfillments': [
            {
                'fid': 0,
                'fulfillment': {
                    'bitmask': 32,
                    'public_key': PUB1,
                    'signature': None,
                    'type': 'fulfillment',
                    'type_id': 4
                },
                'input': None,
                'owners_before': [PUB1]
            }
        ],
        'operation': 'CREATE',
        'timestamp': 42
    },
    'version': 1
}

FFILL2 = {
    'fulfillment': {
        'bitmask': 32,
        'public_key': PUB2,
        'signature': None,
        'type': 'fulfillment',
        'type_id': 4
    },
    'input': {
        'cid': 0,
        'txid': TX1['id']
    },
    'owners_before': [PUB2]
}


@patch('bigchaindb_common.transaction.gen_timestamp', lambda: 42)
class TestBdbCli:
    def test_create_tx(self):
        output = json.loads(invoke_cli(['create_tx', PUB1, PUB2]))
        assert output == TX1

    def test_generate_condition(self):
        output = json.loads(invoke_cli(['generate_condition', PUB2]))
        assert output == COND2

    def test_spend(self):
        output = json.loads(invoke_cli(['spend', json.dumps(TX1)]))
        assert output == FFILL2

    @patch('bdb_transaction_cli.cli.generate_key_pair', lambda: ('a', 'b'))
    def test_generate_keys(self):
        output = invoke_cli(['generate_keys']).rstrip()
        assert output == 'a b'
        output = invoke_cli(['generate_keys', '--type=public']).rstrip()
        assert output == 'b'
        output = invoke_cli(['generate_keys', '--type=private']).rstrip()
        assert output == 'a'


# Here we monkey patch pdb to make it work inside click's CliRunner
pdb.set_trace = pdb.Pdb(stdin=sys.stdin, stdout=sys.stdout).set_trace
