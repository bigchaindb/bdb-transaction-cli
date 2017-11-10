Invocation Examples
===================

These are examples of how to invoke the bdb command, auto-generated from the tests.


create
------
**Usage**

.. code-block:: shell

   Usage: bdb create [OPTIONS] OWNER_BEFORE OUTPUTS

     Generate a CREATE transaction.

     The CREATE transaction creates a new asset.

   Options:
     --metadata JSON
     --asset-data JSON
     --help             Show this message and exit.

.. code-block:: shell

   $ OUTPUTS='{
       "amount": "1",
       "condition": {
           "details": {
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "type": "ed25519-sha-256"
           },
           "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
       },
       "public_keys": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ]
   }'


   $ bdb create 35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF "$OUTPUTS"


create_with_asset
-----------------


.. code-block:: shell

   $ OUTPUTS='{
       "amount": "1",
       "condition": {
           "details": {
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "type": "ed25519-sha-256"
           },
           "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
       },
       "public_keys": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ]
   }'

   $ METADATA='{
       "b": 1
   }'


   $ bdb create --asset-data="$METADATA" 35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF "$OUTPUTS"


generate_keys
-------------
**Usage**

.. code-block:: shell

   Usage: bdb generate_keys [OPTIONS]

     Generate a random Ed25519 key pair.

   Options:
     --name TEXT  Print the keys as shell variables,
                  eg: `export $(bdb generate_keys --name=bob)`
     --help          Show this message and exit.
.. code-block:: shell


   $ bdb generate_keys 


generate_keys_with_name
-----------------------


.. code-block:: shell


   $ bdb generate_keys --name=bob


generate_output
---------------
**Usage**

.. code-block:: shell

   Usage: bdb generate_output [OPTIONS] OWNER_AFTER...

     Generate cryptooutputs from keys.

     Generates a Ed25119 output from a OWNER_AFTER or a ThresholdSha256 Output
     from more than one OWNER_AFTER.

   Options:
     --amount INTEGER  Amount of the asset to output
     --help            Show this message and exit.

.. code-block:: shell


   $ bdb generate_output EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15


get_asset
---------
**Usage**

.. code-block:: shell

   Usage: bdb get_asset [OPTIONS] TRANSACTION

     Return the asset from a transaction for the purpose of providing it as an
     input to `transfer`.

   Options:
     --help  Show this message and exit.

.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null
       },
       "id": "f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0",
       "inputs": [
           {
               "fulfillment": {
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "type": "ed25519-sha-256"
               },
               "fulfills": null,
               "owners_before": [
                   "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
               ]
           }
       ],
       "metadata": null,
       "operation": "CREATE",
       "outputs": [
           {
               "amount": "1",
               "condition": {
                   "details": {
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "type": "ed25519-sha-256"
                   },
                   "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "1.0"
   }'


   $ bdb get_asset "$TRANSACTION"


sign
----
**Usage**

.. code-block:: shell

   Usage: bdb sign [OPTIONS] TRANSACTION PRIVATE_KEY

     Signs a json transaction.

     Signs TRANSACTION (json) with given PRIVATE_KEY. Only a TRANSACTION using
     Ed25519 or ThresholdSha256 outputs can be signed.

     Outputs a signed transaction.

   Options:
     --help  Show this message and exit.

.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null
       },
       "id": "f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0",
       "inputs": [
           {
               "fulfillment": {
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "type": "ed25519-sha-256"
               },
               "fulfills": null,
               "owners_before": [
                   "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
               ]
           }
       ],
       "metadata": null,
       "operation": "CREATE",
       "outputs": [
           {
               "amount": "1",
               "condition": {
                   "details": {
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "type": "ed25519-sha-256"
                   },
                   "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "1.0"
   }'


   $ bdb sign "$TRANSACTION" 3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5


spend
-----
**Usage**

.. code-block:: shell

   Usage: bdb spend [OPTIONS] TRANSACTION [OUTPUT_ID]

     Convert a transaction's outputs to inputs.

     Convert outputs in TRANSACTION (json) to signable/spendable inputs.
     Outputs can individually be selected by passing one or more CONDITION_ID,
     as a JSON list. Otherwise, all outputs are converted.

   Options:
     --help  Show this message and exit.

.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null
       },
       "id": "f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0",
       "inputs": [
           {
               "fulfillment": {
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "type": "ed25519-sha-256"
               },
               "fulfills": null,
               "owners_before": [
                   "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
               ]
           }
       ],
       "metadata": null,
       "operation": "CREATE",
       "outputs": [
           {
               "amount": "1",
               "condition": {
                   "details": {
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "type": "ed25519-sha-256"
                   },
                   "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "1.0"
   }'


   $ bdb spend "$TRANSACTION"


spend_with_condition_ids
------------------------


.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null
       },
       "id": "f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0",
       "inputs": [
           {
               "fulfillment": {
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "type": "ed25519-sha-256"
               },
               "fulfills": null,
               "owners_before": [
                   "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
               ]
           }
       ],
       "metadata": null,
       "operation": "CREATE",
       "outputs": [
           {
               "amount": "1",
               "condition": {
                   "details": {
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "type": "ed25519-sha-256"
                   },
                   "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "1.0"
   }'

   $ OUTPUT_ID='[
       0
   ]'


   $ bdb spend "$TRANSACTION" "$OUTPUT_ID"


transfer
--------
**Usage**

.. code-block:: shell

   Usage: bdb transfer [OPTIONS] INPUTS OUTPUTS ASSET [METADATA]

     Generate a TRANSFER transaction.

     The TRANSFER transaction transfers ownership of a given asset.

   Options:
     --help  Show this message and exit.

.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null
       },
       "id": "f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0",
       "inputs": [
           {
               "fulfillment": {
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "type": "ed25519-sha-256"
               },
               "fulfills": null,
               "owners_before": [
                   "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
               ]
           }
       ],
       "metadata": null,
       "operation": "CREATE",
       "outputs": [
           {
               "amount": "1",
               "condition": {
                   "details": {
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "type": "ed25519-sha-256"
                   },
                   "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "1.0"
   }'


   $ bdb get_asset "$TRANSACTION"


transfer
--------


.. code-block:: shell

   $ INPUTS='[
       {
           "fulfillment": {
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "type": "ed25519-sha-256"
           },
           "fulfills": {
               "output_index": 0,
               "transaction_id": "f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0"
           },
           "owners_before": [
               "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
           ]
       }
   ]'

   $ OUTPUTS='[
       {
           "amount": "1",
           "condition": {
               "details": {
                   "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                   "type": "ed25519-sha-256"
               },
               "uri": "ni:///sha-256;bG2FpGKXhmf46-GOh0FtHAI5OoAvBSvg40790yM-Iik?fpt=ed25519-sha-256&cost=131072"
           },
           "public_keys": [
               "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
           ]
       }
   ]'

   $ ASSET='{
       "id": "f49cad37a04d7179b1181b189108eba71f7a17dae51e97c3efe7dc94d635cea0"
   }'


   $ bdb transfer "$INPUTS" "$OUTPUTS" "$ASSET"
