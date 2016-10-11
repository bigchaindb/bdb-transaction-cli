# -*- coding: utf-8 -*-

import click
# NOTE: We have to import this for pyinstaller.
# FIXME: If this can somehow be removed, with pyinstaller still working. Do so.
import decimal  # noqa
import json

from bigchaindb_common.crypto import generate_key_pair
from bigchaindb_common.transaction import Transaction, Condition


# TODO: Maybe move this into another module
class DictParamType(click.ParamType):
    name = 'JSON'

    def convert(self, value, param, ctx):
        # NOTE: No try-except in case `value is None`, as it is a valid value.
        #       Still we want `json.loads` to visibly fail.
        if value is None:
            return value
        else:
            return json.loads(value)


# TODO: If we can remove those "unnecessary" declarations, we should do so.
#       Couldn't find anything in the click documentation
@click.group()
def spend_group():
    pass


@click.group()
def sign_group():
    pass


@click.group()
def generate_group():
    pass


@generate_group.group('generate')
def generate_sub_group():
    """Generate keys, conditions or transactions."""
    pass


@generate_sub_group.command('keys')
@click.option('--type', 'key_type', type=click.Choice(['private', 'public']))
def generate_keys(key_type):
    """Generate a random pair of Ed25519 keys.

        Generates a random Ed25519 key pair separated by a space character.
        First value is the private key, second is the public key.
    """
    private_key, public_key = generate_key_pair()

    if key_type == 'private':
        click.echo(private_key)
    elif key_type == 'public':
        click.echo(public_key)
    else:
        click.echo('{} {}'.format(private_key, public_key))


# TODO:
#       - There is no way to define weights at this point
#       - There is no way to generate a deeply nested condition
@generate_sub_group.command('condition')
@click.argument('owner_after', required=True, nargs=-1)
def generate_condition(owner_after):
    """Generate Cryptoconditions from keys.

        Generates a Ed25119 condition from a OWNER_AFTER or a ThresholdSha256
        Condition from more than one OWNER_AFTER.
    """
    condition = Condition.generate(list(owner_after))
    click.echo(json.dumps(condition.to_dict()))


@generate_sub_group.command()
@click.argument('owner_before', nargs=1)
@click.argument('owner_after', required=True, nargs=-1)
@click.option('--payload', '-P', required=False, type=DictParamType(),
              help='A payload to be included in the transaction.')
# TODO:
#       Instead of taking `owner_after`, this command should just be taking
#       JSONified conditions from `generate condition` to unify this command
#       with the future `generate transfer` command.
def create(owner_before, owner_after, payload):
    """Generate an unsigned `CREATE` transaction.

        Generates a `CREATE` transaction that creates an asset from the
        OWNER_BEFORE to one or more OWNER_AFTER.
    """
    transaction = Transaction.create([owner_before], list(owner_after),
                                     payload)
    # TODO: Use `str`:
    #           - https://github.com/bigchaindb/bigchaindb-common/issues/37
    transaction = Transaction._to_str(transaction.to_dict())
    click.echo(transaction)


@spend_group.command()
@click.argument('transaction', type=DictParamType())
@click.argument('condition_id', required=False, type=click.INT, nargs=-1)
# TODO: option to output JSON list
def spend(transaction, condition_id):
    """Convert a transaction's outputs to inputs.

        Converts a TRANSACTION's conditions to signable/spendable fulfillments.
        Conditions can individually selected by passing one or more
        CONDITION_ID. Otherwise, all conditions are converted.
    """
    transaction = Transaction.from_dict(transaction)
    inputs = transaction.to_inputs(list(condition_id))
    inputs = [json.dumps(i.to_dict()) for i in inputs]
    # NOTE: We intentionally we don't output a JSON list here, as `transfer`
    #       accepts this methods output as variadic argument.
    #       To learn more about this, visit:
    #       http://click.pocoo.org/5/arguments/#variadic-arguments
    click.echo(' '.join(inputs))


@sign_group.command()
@click.argument('transaction', type=DictParamType())
@click.argument('private_key', required=True, nargs=-1)
def sign(transaction, private_key):
    """Sign a transaction.

        Sign a TRANSACTION <json> with one more more PRIVATE_KEY. Only a
        TRANSACTION using Ed25519 or ThresholdSha256 conditions can be signed.
    """
    transaction = Transaction.from_dict(transaction)
    transaction = transaction.sign(list(private_key))
    # TODO: Use `str`:
    #           - https://github.com/bigchaindb/bigchaindb-common/issues/37
    transaction = Transaction._to_str(transaction.to_dict())
    click.echo(transaction)


main = click.CommandCollection(
    sources=[spend_group, generate_group, sign_group])


if __name__ == '__main__':
    main()
