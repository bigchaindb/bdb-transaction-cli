#!/usr/bin/env python

import json
import pdb
import sys
from unittest.mock import patch

from click.testing import CliRunner

from bdb_transaction_cli import cli


PUB1 = 'HEAMTn6m366gBJ51PhuZ3t7WiX2GhhqiMfAbEzgvAm2v'
PRIV1 = '9zcUmfAtdhHhMZNbKPy6RZgzSBb7QruXAZxGeydswBXA'

PUB2 = '7YMPkiF1m1mFrEaJbvFF4rS7ExgaL93jvJCx1VhN65AA'
PRIV2 = '8qhgK24XUNwpSqa8SMQeTYwXYBrJDMchJWSazZ1yp4dm'


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
        'uri': 'cc:4:20:YS4vLbWV2RJ5ETZj-7R2jadaGsmG24dZ0iGe3B09PLs:96'
    },
    'owners_after': [PUB2]
}


TX1 = {
    'id': '223327307af7ed62ab695d1c14332544deb7aa123b0f242108e109267e0daf3d',
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


@patch('bigchaindb_common.transaction.gen_timestamp', lambda: 42)
class TestBdbCli:
    def test_create_tx(self):
        output = json.loads(invoke_cli(['create_tx', PUB1, PUB2]))
        assert output == TX1

    def test_generate_condition(self):
        output = json.loads(invoke_cli(['generate_condition', PUB2]))
        assert output == COND2


# Here we monkey patch pdb to make it work inside click's CliRunner
pdb.set_trace = pdb.Pdb(stdin=sys.stdin, stdout=sys.stdout).set_trace
