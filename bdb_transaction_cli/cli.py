import json

import click
from bigchaindb.common.crypto import generate_key_pair
from bigchaindb.common.transaction import Transaction, \
    Condition, Fulfillment, Metadata, Asset, Ed25519Fulfillment

from bdb_transaction_cli.utils import json_argument, json_option, listify


@click.group()
def main():
    pass


@main.command()
@click.option('--name', required=False, help=(
    "Print the keys as shell variables,                             eg: "
    "`export $(bdb generate_keys --name=bob)`"))
def generate_keys(name):
    """
    Generate a random Ed25519 key pair.
    """
    priv, pub = generate_key_pair()
    if name:
        fmt = '{name}_pub={pub} {name}_priv={priv}'
        click.echo(fmt.format(name=name, pub=pub, priv=priv))
    else:
        click.echo(json.dumps({'public': pub, 'private': priv}))


@main.command()
@click.argument('owner_after', required=True, nargs=-1)
def generate_condition(owner_after):
    """
    Generate cryptoconditions from keys.

    Generates a Ed25119 condition from a OWNER_AFTER or a ThresholdSha256
    Condition from more than one OWNER_AFTER.
    """
    condition = Condition.generate(list(owner_after))
    click.echo(json.dumps(condition.to_dict()))


@main.command()
@click.argument('owner_before')
@json_argument('conditions')
@json_option('--metadata')
@json_option('--asset')
def create(owner_before, conditions, metadata, asset):
    """
    Generate a CREATE transaction.

    The CREATE transaction creates a new asset.
    """
    ffill = Fulfillment(Ed25519Fulfillment(public_key=owner_before),
                        [owner_before])
    conditions = [Condition.from_dict(c) for c in listify(conditions)]
    asset = Asset.from_dict(asset) if asset else None
    tx = Transaction(Transaction.CREATE, asset, [ffill],
                     conditions, metadata)
    tx = Transaction._to_str(tx.to_dict())
    click.echo(tx)


@main.command()
@json_argument('transaction')
@json_argument('condition_id', required=False)
def spend(transaction, condition_id):
    """
    Convert a transaction's outputs to inputs.

    Convert conditions in TRANSACTION (json) to signable/spendable
    fulfillments. Conditions can individually be selected by passing one or
    more CONDITION_ID, as a JSON list. Otherwise, all conditions are converted.
    """
    transaction = Transaction.from_dict(transaction)
    inputs = transaction.to_inputs(condition_id)
    click.echo(json.dumps([i.to_dict() for i in inputs]))


@main.command()
@json_argument('transaction')
@click.argument('private_key')
def sign(transaction, private_key):
    """
    Signs a json transaction.

    Signs TRANSACTION (json) with given PRIVATE_KEY. Only a
    TRANSACTION using Ed25519 or ThresholdSha256 conditions can be signed.

    Outputs a signed transaction.
    """
    transaction = Transaction.from_dict(transaction)
    transaction = transaction.sign([private_key])
    transaction = Transaction._to_str(transaction.to_dict())
    click.echo(transaction)


@main.command()
@json_argument('fulfillments')
@json_argument('conditions')
@json_argument('asset')
@json_argument('metadata', required=False)
def transfer(fulfillments, conditions, asset, metadata):
    """
    Generate a TRANSFER transaction.

    The TRANSFER transaction transfers ownership of a given asset.
    """
    tx = Transaction(Transaction.TRANSFER,
                     asset=Asset(asset),
                     metadata=Metadata(metadata))
    for f in listify(fulfillments):
        tx.add_fulfillment(Fulfillment.from_dict(f))
    for c in listify(conditions):
        tx.add_condition(Condition.from_dict(c))
    click.echo(Transaction._to_str(tx.to_dict()))


@main.command()
@json_argument('transaction')
def get_asset(transaction):
    """
    Return the asset from a transaction for the purpose of providing it as an
    input to `transfer`.
    """
    click.echo(json.dumps({"id": transaction['transaction']['asset']['id']}))
