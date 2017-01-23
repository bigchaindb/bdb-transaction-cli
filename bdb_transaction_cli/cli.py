import json

import click
from bigchaindb.common.crypto import generate_key_pair
from bigchaindb.common.transaction import Transaction, Output, Input

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
@click.option('--amount', required=False, default=1,
              help="Amount of the asset to output")
@click.argument('owner_after', required=True, nargs=-1)
def generate_output(amount, owner_after):
    """
    Generate cryptooutputs from keys.

    Generates a Ed25119 output from a OWNER_AFTER or a ThresholdSha256
    Output from more than one OWNER_AFTER.
    """
    output = Output.generate(list(owner_after), amount=amount)
    click.echo(json.dumps(output.to_dict()))


@main.command()
@click.argument('owner_before')
@json_argument('outputs')
@json_option('--metadata')
@json_option('--asset-data')
def create(owner_before, outputs, metadata, asset_data):
    """
    Generate a CREATE transaction.

    The CREATE transaction creates a new asset.
    """
    input = Input.generate([owner_before])
    outputs = [Output.from_dict(c) for c in listify(outputs)]
    tx = Transaction(Transaction.CREATE, {"data": asset_data},
                     [input], outputs, metadata)
    tx = Transaction._to_str(tx.to_dict())
    click.echo(tx)


@main.command()
@json_argument('transaction')
@json_argument('output_id', required=False)
def spend(transaction, output_id):
    """
    Convert a transaction's outputs to inputs.

    Convert outputs in TRANSACTION (json) to signable/spendable
    inputs. Outputs can individually be selected by passing one or
    more CONDITION_ID, as a JSON list. Otherwise, all outputs are converted.
    """
    transaction = Transaction.from_dict(transaction)
    inputs = transaction.to_inputs(output_id)
    click.echo(json.dumps([i.to_dict() for i in inputs]))


@main.command()
@json_argument('transaction')
@click.argument('private_key')
def sign(transaction, private_key):
    """
    Signs a json transaction.

    Signs TRANSACTION (json) with given PRIVATE_KEY. Only a
    TRANSACTION using Ed25519 or ThresholdSha256 outputs can be signed.

    Outputs a signed transaction.
    """
    transaction = Transaction.from_dict(transaction)
    transaction = transaction.sign([private_key])
    transaction = Transaction._to_str(transaction.to_dict())
    click.echo(transaction)


@main.command()
@json_argument('inputs')
@json_argument('outputs')
@json_argument('asset')
@json_argument('metadata', required=False)
def transfer(inputs, outputs, asset, metadata):
    """
    Generate a TRANSFER transaction.

    The TRANSFER transaction transfers ownership of a given asset.
    """
    inputs = [Input.from_dict(i) for i in listify(inputs)]
    outputs = [Output.from_dict(i) for i in listify(outputs)]
    tx = Transaction(Transaction.TRANSFER,
                     asset=asset,
                     inputs=inputs,
                     outputs=outputs,
                     metadata=metadata)
    click.echo(Transaction._to_str(tx.to_dict()))


@main.command()
@json_argument('transaction')
def get_asset(transaction):
    """
    Return the asset from a transaction for the purpose of providing it as an
    input to `transfer`.
    """
    click.echo(json.dumps({"id": transaction['asset']['id']}))
