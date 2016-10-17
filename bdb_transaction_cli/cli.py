import click
import json

from bigchaindb_common.crypto import generate_key_pair
from bigchaindb_common.transaction import Transaction, \
    Condition, Fulfillment, Metadata, Asset, Ed25519Fulfillment

from bdb_transaction_cli.utils import json_argument, listify


@click.group()
def main():
    pass


# TODO: env output option
@main.command()
def generate_keys():
    """
    Generate Ed25519 key pair.

    Generates a random Ed25519 key pair separated by a space character.
    First value is the private key, second is the public key.
    """
    private_key, public_key = generate_key_pair()
    click.echo('{} {}'.format(private_key, public_key))


# TODO:
#       - There is no way to define weights at this point
#       - There is no way to generate a deeply nested condition
@main.command()
@click.argument('owner_after', required=True, nargs=-1)
def generate_condition(owner_after):
    """
    Generate Cryptoconditions from keys.

    Generates a Ed25119 condition from a OWNER_AFTER or a ThresholdSha256
    Condition from more than one OWNER_AFTER.
    """
    condition = Condition.generate(list(owner_after))
    click.echo(json.dumps(condition.to_dict()))


@main.command()
@click.argument('node_pubkey')
@json_argument('conditions', required=True)
@json_argument('metadata', '-m', required=False,
               help='Metadata to be included in the transaction.')
def create(node_pubkey, conditions, metadata):
    """
    Generate a `CREATE` transaction.

    Generates a `CREATE` transaction that creates an asset, to be signed
    off by the federation node having NODE_PUBKEY and to be owned by
    OWNER_PUBKEY.
    """
    # TODO: user can pass asset
    # TODO: Fix docstring
    ffill = Fulfillment(Ed25519Fulfillment(public_key=node_pubkey),
                        [node_pubkey])
    conditions = [Condition.from_dict(c) for c in listify(conditions)]
    tx = Transaction(Transaction.CREATE, None, [ffill],
                     conditions, metadata)
    tx = Transaction._to_str(tx.to_dict())
    click.echo(tx)


@main.command()
@json_argument('transaction')
@click.argument('condition_id', required=False, type=click.INT)
# TODO: option to output JSON list
def spend(transaction, condition_id):
    """
    Convert a transaction's outputs to inputs.

    Convert conditions in TRANSACTION (json) to signable/spendable
    fulfillments. Conditions can individually selected by passing one or more
    CONDITION_ID. Otherwise, all conditions are converted.
    """
    transaction = Transaction.from_dict(transaction)
    inputs = transaction.to_inputs(list(condition_id))
    inputs = [json.dumps(i.to_dict()) for i in inputs]
    # jsonize
    # NOTE: We intentiod4dnally we don't output a JSON list here, as `transfer`
    #       accepts this methods output as variadic argument.
    #       To learn more about this, visit:
    #       http://click.pocoo.org/5/arguments/#variadic-arguments
    click.echo(' '.join(inputs))


@main.command()
@json_argument('transaction')
@click.argument('private_key', required=True, nargs=-1)
def sign(transaction, private_key):
    """
    Signs a json transaction.

    Signs TRANSACTION (json) with one more more PRIVATE_KEY. Only a
    TRANSACTION using Ed25519 or ThresholdSha256 conditions can be signed.

    Outputs a signed transaction.
    """
    transaction = Transaction.from_dict(transaction)
    transaction = transaction.sign(list(private_key))
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
    """
    tx = Transaction(Transaction.TRANSFER,
                     asset=Asset(asset),
                     metadata=Metadata(metadata))
    for f in listify(fulfillments):
        tx.add_fulfillment(Fulfillment.from_dict(f))
    print(conditions)
    for c in listify(conditions):
        tx.add_condition(Condition.from_dict(c))
    print(Transaction._to_str(tx.to_dict()))
