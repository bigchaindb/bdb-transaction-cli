Invocation Examples
===================

These are examples of how to invoke the bdb command, auto-generated from the tests.


create
------


.. code-block:: shell

   $ CONDITIONS='{
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
       "owners_after": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ]
   }'


   $ bdb create 35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF "$CONDITIONS"


create_with_asset
-----------------


.. code-block:: shell

   $ CONDITIONS='{
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
       "owners_after": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ]
   }'

   $ METADATA='{
       "data": {
           "b": 1
       },
       "divisible": false,
       "id": "a",
       "refillable": false,
       "updatable": false
   }'


   $ bdb create --asset="$METADATA" 35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF "$CONDITIONS"


generate_condition
------------------


.. code-block:: shell


   $ bdb generate_condition EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15


generate_keys
-------------


.. code-block:: shell


   $ bdb generate_keys 


generate_keys_with_name
-----------------------


.. code-block:: shell


   $ bdb generate_keys --name=bob


get_asset
---------


.. code-block:: shell

   $ TRANSACTION='{
       "id": "58aa63812a06caf9d4ea3d915b7e97ef7e554e712bbcd694d686b540201d64ad",
       "transaction": {
           "asset": {
               "data": null,
               "divisible": false,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "refillable": false,
               "updatable": false
           },
           "conditions": [
               {
                   "amount": 1,
                   "cid": 0,
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
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ]
               }
           ],
           "fulfillments": [
               {
                   "fid": 0,
                   "fulfillment": {
                       "bitmask": 32,
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "input": null,
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ]
               }
           ],
           "metadata": null,
           "operation": "CREATE"
       },
       "version": 1
   }'


   $ bdb get_asset "$TRANSACTION"


sign
----


.. code-block:: shell

   $ TRANSACTION='{
       "id": "58aa63812a06caf9d4ea3d915b7e97ef7e554e712bbcd694d686b540201d64ad",
       "transaction": {
           "asset": {
               "data": null,
               "divisible": false,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "refillable": false,
               "updatable": false
           },
           "conditions": [
               {
                   "amount": 1,
                   "cid": 0,
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
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ]
               }
           ],
           "fulfillments": [
               {
                   "fid": 0,
                   "fulfillment": {
                       "bitmask": 32,
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "input": null,
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ]
               }
           ],
           "metadata": null,
           "operation": "CREATE"
       },
       "version": 1
   }'


   $ bdb sign "$TRANSACTION" 3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5


spend
-----


.. code-block:: shell

   $ TRANSACTION='{
       "id": "58aa63812a06caf9d4ea3d915b7e97ef7e554e712bbcd694d686b540201d64ad",
       "transaction": {
           "asset": {
               "data": null,
               "divisible": false,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "refillable": false,
               "updatable": false
           },
           "conditions": [
               {
                   "amount": 1,
                   "cid": 0,
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
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ]
               }
           ],
           "fulfillments": [
               {
                   "fid": 0,
                   "fulfillment": {
                       "bitmask": 32,
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "input": null,
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ]
               }
           ],
           "metadata": null,
           "operation": "CREATE"
       },
       "version": 1
   }'


   $ bdb spend "$TRANSACTION"


spend_with_condition_ids
------------------------


.. code-block:: shell

   $ TRANSACTION='{
       "id": "58aa63812a06caf9d4ea3d915b7e97ef7e554e712bbcd694d686b540201d64ad",
       "transaction": {
           "asset": {
               "data": null,
               "divisible": false,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "refillable": false,
               "updatable": false
           },
           "conditions": [
               {
                   "amount": 1,
                   "cid": 0,
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
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ]
               }
           ],
           "fulfillments": [
               {
                   "fid": 0,
                   "fulfillment": {
                       "bitmask": 32,
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "type": "fulfillment",
                       "type_id": 4
                   },
                   "input": null,
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ]
               }
           ],
           "metadata": null,
           "operation": "CREATE"
       },
       "version": 1
   }'

   $ CONDITION_ID='[
       0
   ]'


   $ bdb spend "$TRANSACTION" "$CONDITION_ID"


transfer
--------


.. code-block:: shell

   $ FULFILLMENTS='[
       {
           "fulfillment": {
               "bitmask": 32,
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "type": "fulfillment",
               "type_id": 4
           },
           "input": {
               "cid": 0,
               "txid": "58aa63812a06caf9d4ea3d915b7e97ef7e554e712bbcd694d686b540201d64ad"
           },
           "owners_before": [
               "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
           ]
       }
   ]'

   $ CONDITIONS='{
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
       "owners_after": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ]
   }'

   $ ASSET='{}'


   $ bdb transfer "$FULFILLMENTS" "$CONDITIONS" "$ASSET"
