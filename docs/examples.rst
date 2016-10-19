Invocation Examples
===================

These are examples of how to invoke the bdb command, auto-generated from the tests.


create
------


.. code-block:: shell

   $ CONDITIONS='{
       "owners_after": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ],
       "amount": 1,
       "condition": {
           "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96",
           "details": {
               "type_id": 4,
               "type": "fulfillment",
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "bitmask": 32
           }
       }
   }'


   $ bdb create 35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF '$CONDITIONS'


create_with_asset
-----------------


.. code-block:: shell

   $ CONDITIONS='{
       "owners_after": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ],
       "amount": 1,
       "condition": {
           "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96",
           "details": {
               "type_id": 4,
               "type": "fulfillment",
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "bitmask": 32
           }
       }
   }'


   $ bdb create 35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF '$CONDITIONS' --asset={"data": {"b": 1}, "id": "a", "updatable": true, "divisible": false, "refillable": false}


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
       "transaction": {
           "fulfillments": [
               {
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ],
                   "fid": 0,
                   "input": null,
                   "fulfillment": {
                       "type_id": 4,
                       "type": "fulfillment",
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "bitmask": 32
                   }
               }
           ],
           "conditions": [
               {
                   "cid": 0,
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ],
                   "condition": {
                       "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96",
                       "details": {
                           "type_id": 4,
                           "type": "fulfillment",
                           "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                           "signature": null,
                           "bitmask": 32
                       }
                   },
                   "amount": 1
               }
           ],
           "asset": {
               "data": null,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "updatable": false,
               "divisible": false,
               "refillable": false
           },
           "metadata": null,
           "operation": "CREATE",
           "timestamp": 42
       },
       "id": "db3a077a24625b0c56d0e8db9cb5a75d48e62a9a2119b299603533d6eb99df99",
       "version": 1
   }'


   $ bdb get_asset '$TRANSACTION'


sign
----


.. code-block:: shell

   $ TRANSACTION='{
       "transaction": {
           "fulfillments": [
               {
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ],
                   "fid": 0,
                   "input": null,
                   "fulfillment": {
                       "type_id": 4,
                       "type": "fulfillment",
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "bitmask": 32
                   }
               }
           ],
           "conditions": [
               {
                   "cid": 0,
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ],
                   "condition": {
                       "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96",
                       "details": {
                           "type_id": 4,
                           "type": "fulfillment",
                           "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                           "signature": null,
                           "bitmask": 32
                       }
                   },
                   "amount": 1
               }
           ],
           "asset": {
               "data": null,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "updatable": false,
               "divisible": false,
               "refillable": false
           },
           "metadata": null,
           "operation": "CREATE",
           "timestamp": 42
       },
       "id": "db3a077a24625b0c56d0e8db9cb5a75d48e62a9a2119b299603533d6eb99df99",
       "version": 1
   }'


   $ bdb sign '$TRANSACTION' 3sJ8iqyVE2jJAQiHRKXaHq4arsUPQgVKv3mA4uRKeYG5


spend
-----


.. code-block:: shell

   $ TRANSACTION='{
       "transaction": {
           "fulfillments": [
               {
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ],
                   "fid": 0,
                   "input": null,
                   "fulfillment": {
                       "type_id": 4,
                       "type": "fulfillment",
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "bitmask": 32
                   }
               }
           ],
           "conditions": [
               {
                   "cid": 0,
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ],
                   "condition": {
                       "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96",
                       "details": {
                           "type_id": 4,
                           "type": "fulfillment",
                           "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                           "signature": null,
                           "bitmask": 32
                       }
                   },
                   "amount": 1
               }
           ],
           "asset": {
               "data": null,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "updatable": false,
               "divisible": false,
               "refillable": false
           },
           "metadata": null,
           "operation": "CREATE",
           "timestamp": 42
       },
       "id": "db3a077a24625b0c56d0e8db9cb5a75d48e62a9a2119b299603533d6eb99df99",
       "version": 1
   }'


   $ bdb spend '$TRANSACTION'


spend_with_condition_ids
------------------------


.. code-block:: shell

   $ TRANSACTION='{
       "transaction": {
           "fulfillments": [
               {
                   "owners_before": [
                       "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF"
                   ],
                   "fid": 0,
                   "input": null,
                   "fulfillment": {
                       "type_id": 4,
                       "type": "fulfillment",
                       "public_key": "35qDXhZTUvna23NLc1hMfmrgPniBwPgNjko1VfQuD3vF",
                       "signature": null,
                       "bitmask": 32
                   }
               }
           ],
           "conditions": [
               {
                   "cid": 0,
                   "owners_after": [
                       "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
                   ],
                   "condition": {
                       "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96",
                       "details": {
                           "type_id": 4,
                           "type": "fulfillment",
                           "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
                           "signature": null,
                           "bitmask": 32
                       }
                   },
                   "amount": 1
               }
           ],
           "asset": {
               "data": null,
               "id": "cab78dc6-1cb2-4bc0-8ec2-267dedb5fa0f",
               "updatable": false,
               "divisible": false,
               "refillable": false
           },
           "metadata": null,
           "operation": "CREATE",
           "timestamp": 42
       },
       "id": "db3a077a24625b0c56d0e8db9cb5a75d48e62a9a2119b299603533d6eb99df99",
       "version": 1
   }'

   $ CONDITION_ID='[
       0
   ]'


   $ bdb spend '$TRANSACTION' '$CONDITION_ID'


transfer
--------


.. code-block:: shell

   $ FULFILLMENTS='[
       {
           "owners_before": [
               "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
           ],
           "input": {
               "cid": 0,
               "txid": "db3a077a24625b0c56d0e8db9cb5a75d48e62a9a2119b299603533d6eb99df99"
           },
           "fulfillment": {
               "type_id": 4,
               "type": "fulfillment",
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "bitmask": 32
           }
       }
   ]'

   $ CONDITIONS='{
       "owners_after": [
           "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15"
       ],
       "amount": 1,
       "condition": {
           "uri": "cc:4:20:zL3F_XLRs_snrfmdqSFPqEcu-bu1xF6636oSYpNWvIw:96",
           "details": {
               "type_id": 4,
               "type": "fulfillment",
               "public_key": "EnE1QD5kBY9Zrsp2Ejsp7W7ZMFAcH75SqR9wz6WrUR15",
               "signature": null,
               "bitmask": 32
           }
       }
   }'

   $ ASSET='{}'


   $ bdb transfer '$FULFILLMENTS' '$CONDITIONS' '$ASSET'
