#!/usr/bin/env python

import copy
import json
import pdb
import sys
from unittest.mock import patch

import pytest
from bigchaindb_common.exceptions import KeypairMismatchException
from click.testing import CliRunner

from bdb_transaction_cli import cli


PUB1 = '35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF'
PRIV1 = '3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5'

PUB2 = 'EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15'
PRIV2 = 'HrQWRzMwGfLJHkQsaXMef7beMTV4M5aynK4Xm1roFq5V'


def invoke_method(args):
    args = [json.dumps(arg) if type(arg) in (dict, list)
            else arg for arg in args]
    runner = CliRunner()
    result = runner.invoke(cli.main, args)
    if result.exit_code != 0:
        print(result.output, file=sys.stderr)
        raise result.exception
    return result.output


def test_command_line_interface():
    output = invoke_method([])
    assert output.startswith('Usage:')


COND2 = {
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
    'owners_after': [PUB2]
}

COND2_WITH_ID = copy.copy(COND2)
COND2_WITH_ID['cid'] = 0


ASSET = {
    "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
    "data": None,
    "updatable": False,
    "divisible": False,
    "refillable": False
}


TX_CREATE = {
    'id': 'db3a077a24625b0c56d0e8db9cb5a75d48e62a9a2119b299603533d6eb99df99',
    'transaction': {
        'conditions': [COND2_WITH_ID],
        'metadata': None,
        "asset": ASSET,
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
        'txid': TX_CREATE['id']
    },
    'owners_before': [PUB2]
}

FFILL2_WITH_ID = copy.copy(FFILL2)
FFILL2_WITH_ID['fid'] = 0


TX_CREATE_SIGNED = {
    'id': 'db3a077a24625b0c56d0e8db9cb5a75d48e62a9a2119b299603533d6eb99df99',
    'transaction': {
        'conditions': [COND2_WITH_ID],
        'metadata': None,
        "asset": ASSET,
        'fulfillments': [
            {
                'fid': 0,
                'fulfillment': 'cf:4:HvQ3Eg9U6Crw-DFf2v36GaPYsEMLhBSSZEuXNQ6cZFhFiCQyFc_LY90Wcqoli3lvBmHctwZJQ6rlBt5tt83M32x7PNiWQ-agikVpij3i1xPI8tikeQuIdoaBzhaU-mEH',  # noqa
                'input': None,
                'owners_before': [PUB1]
            }
        ],
        'operation': 'CREATE',
        'timestamp': 42
    },
    'version': 1
}


TX_TRANSFER = {
    "id": "a86830c6685df71a882c678fe856e44f1a5afdf86483a50c746236cf4c92d050",
    "version": 1,
    "transaction": {
        "operation": "TRANSFER",
        "conditions": [COND2_WITH_ID],
        "fulfillments": [FFILL2_WITH_ID],
        "asset": {"id": ASSET['id']},
        "metadata": None,
        "timestamp": 42
    }
}


@patch('bigchaindb_common.transaction.gen_timestamp', lambda: 42)
@patch('bigchaindb_common.transaction.Asset.to_hash', lambda self: ASSET['id'])
@patch('bdb_transaction_cli.cli.generate_key_pair', lambda: ('b', 'a'))
class TestBdbCli:
    def test_create(self):
        output = json.loads(invoke_method(['create', PUB1, COND2]))
        assert output == TX_CREATE

    def test_generate_condition(self):
        output = json.loads(invoke_method(['generate_condition', PUB2]))
        assert output == COND2

    def test_spend(self):
        output = json.loads(invoke_method(['spend', TX_CREATE]))
        assert output == [FFILL2]

    def test_spend_with_condition_ids(self):
        output = json.loads(invoke_method(['spend', TX_CREATE, '[0]']))
        assert output == [FFILL2]

    def test_generate_keys(self):
        output = invoke_method(['generate_keys']).rstrip()
        assert output == 'a b'

    def test_generate_keys_with_name(self):
        output = invoke_method(['generate_keys', '--name=bob']).rstrip()
        assert output == 'bob_pub=a bob_priv=b'

    def test_sign(self):
        output = json.loads(invoke_method(['sign', TX_CREATE, PRIV1]))
        assert output == TX_CREATE_SIGNED

    def test_sign_fails(self):
        with pytest.raises(KeypairMismatchException):
            invoke_method(['sign', TX_CREATE, PRIV2])

    def test_transfer(self):
        args = ['transfer', [FFILL2], COND2, '{}']
        output = json.loads(invoke_method(args))
        assert output == TX_TRANSFER


# Here we monkey patch pdb to make it work inside click's CliRunner
pdb.set_trace = pdb.Pdb(stdin=sys.stdin, stdout=sys.stdout).set_trace
