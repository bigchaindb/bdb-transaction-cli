import click
import json

from bigchaindb_common.crypto import generate_key_pair
from bigchaindb_common.transaction import Transaction, Condition

from bdb_transaction_cli.utils import JsonParamType


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
@click.argument('owner_before', nargs=1)
@click.argument('owner_after', required=True, nargs=-1)
@click.option('--payload', '-P', required=False, type=JsonParamType(),
              help='A payload to be included in the transaction.')
# TODO:
#       Instead of taking `owner_after`, this command should just be taking
#       JSONified conditions from `generate condition` to unify this command
#       with the future `generate transfer` command.
def create_tx(owner_before, owner_after, payload):
    """
    Generate a `CREATE` transaction.

    Generates a `CREATE` transaction that creates an asset from the
    OWNER_BEFORE to one or more OWNER_AFTER.
    """
    transaction = Transaction.create([owner_before], list(owner_after),
                                     payload)
    transaction = Transaction._to_str(transaction.to_dict())
    click.echo(transaction)


@main.command()
@click.argument('transaction', type=JsonParamType())
@click.argument('condition_id', required=False, type=click.INT, nargs=-1)
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
@click.argument('transaction', type=JsonParamType())
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
    # TODO: Use `str`:
    #           - https://github.com/bigchaindb/bigchaindb-common/issues/37
    transaction = Transaction._to_str(transaction.to_dict())
    click.echo(transaction)


# TODO: bdb transfer '[.. ffills]' '[.. conditions]' '[payload]'
