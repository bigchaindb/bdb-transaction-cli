Invocation Examples
===================

These are examples of how to invoke the bdb command, auto-generated from the tests.


create
------


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


.. code-block:: shell


   $ bdb generate_keys 


generate_keys_with_name
-----------------------


.. code-block:: shell


   $ bdb generate_keys --name=bob


generate_output
---------------


.. code-block:: shell


   $ bdb generate_output EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15


get_asset
---------


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
