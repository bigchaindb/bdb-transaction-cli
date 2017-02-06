Invocation Examples
===================

These are examples of how to invoke the bdb command, auto-generated from the tests.


create
------


.. code-block:: shell

   $ OUTPUTS='{
       "amount": 1,
       "condition": {
           "details": {
               "bitmask": 32,
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "type": "fulfillment",
               "type_id": 4
           },
           "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96"
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
       "amount": 1,
       "condition": {
           "details": {
               "bitmask": 32,
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "type": "fulfillment",
               "type_id": 4
           },
           "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96"
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
           "data": null,
           "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23"
       },
       "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23",
       "inputs": [
           {
               "fulfillment": {
                   "bitmask": 32,
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "signature": null,
                   "type": "fulfillment",
                   "type_id": 4
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
               "amount": 1,
               "condition": {
                   "details": {
                       "bitmask": 32,
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "0.9"
   }'


   $ bdb get_asset "$TRANSACTION"


sign
----


.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null,
           "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23"
       },
       "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23",
       "inputs": [
           {
               "fulfillment": {
                   "bitmask": 32,
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "signature": null,
                   "type": "fulfillment",
                   "type_id": 4
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
               "amount": 1,
               "condition": {
                   "details": {
                       "bitmask": 32,
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "0.9"
   }'


   $ bdb sign "$TRANSACTION" 3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5


spend
-----


.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null,
           "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23"
       },
       "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23",
       "inputs": [
           {
               "fulfillment": {
                   "bitmask": 32,
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "signature": null,
                   "type": "fulfillment",
                   "type_id": 4
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
               "amount": 1,
               "condition": {
                   "details": {
                       "bitmask": 32,
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "0.9"
   }'


   $ bdb spend "$TRANSACTION"


spend_with_condition_ids
------------------------


.. code-block:: shell

   $ TRANSACTION='{
       "asset": {
           "data": null,
           "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23"
       },
       "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23",
       "inputs": [
           {
               "fulfillment": {
                   "bitmask": 32,
                   "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                   "signature": null,
                   "type": "fulfillment",
                   "type_id": 4
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
               "amount": 1,
               "condition": {
                   "details": {
                       "bitmask": 32,
                       "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96"
               },
               "public_keys": [
                   "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
               ]
           }
       ],
       "version": "0.9"
   }'

   $ OUTPUT_ID='[
       0
   ]'


   $ bdb spend "$TRANSACTION" "$OUTPUT_ID"


transfer
--------


.. code-block:: shell

   $ INPUTS='[
       {
           "fulfillment": {
               "bitmask": 32,
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "type": "fulfillment",
               "type_id": 4
           },
           "fulfills": {
               "output": 0,
               "txid": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23"
           },
           "owners_before": [
               "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
           ]
       }
   ]'

   $ OUTPUTS='[
       {
           "amount": 1,
           "condition": {
               "details": {
                   "bitmask": 32,
                   "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                   "signature": null,
                   "type": "fulfillment",
                   "type_id": 4
               },
               "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96"
           },
           "public_keys": [
               "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
           ]
       }
   ]'

   $ ASSET='{
       "data": null,
       "id": "211230736e0b7d08af98d222c01170a45b0e3aebb10a40f07751512ed171eb23"
   }'


   $ bdb transfer "$INPUTS" "$OUTPUTS" "$ASSET"
