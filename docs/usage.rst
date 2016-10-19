=====
Usage
=====

Here is demonstrated how Alice can make two transactions, first to
create an asset, and then to transfer it to Bob.

Creating an asset
=================

The below diagram shows how to generate a transaction that creates an
asset.

The required inputs to be able to do this are the public key of the
validating node (server) that the transaction will be first submitted
to.

.. graphviz::

    digraph CREATE {
	size = 10;
	rankdir=LR;
	node [fontname="helvetica"];
	node [color=red]

	{ // Inputs (non processes)
	    node [shape=record]
	    node [color=black]
	    condition
	    pubkey_alice
	    privkey_alice
	    author_pubkey
            asset [style=dashed]
            metadata [style=dashed]
	    CREATE_transaction
	    signed_transaction
	}
	
	{
	    pubkey_alice -> generate_condition
	    generate_condition -> condition
	    condition -> create
	    author_pubkey -> create
            asset -> create
            metadata -> create
	    create -> CREATE_transaction
	    generate_keys -> pubkey_alice
	    generate_keys -> privkey_alice
	    privkey_alice -> sign
	    CREATE_transaction -> sign
	    sign -> signed_transaction
	}

	{ rank=same pubkey_alice privkey_alice }
    }


Transferring an asset
=====================

The below diagram shows how to generate a transaction that transfers an
asset. 

.. graphviz::

    digraph TRANSFER {
	size = 10;
	rankdir=LR;
	node [fontname="helvetica"];
	node [color=red]

	{ // Inputs (non processes)
	    node [shape=record]
	    node [color=black]
	    condition
	    pubkey_alice [fontcolor=grey]
	    privkey_alice
	    pubkey_bob
	    privkey_bob [fontcolor=grey]
	    CREATE_transaction
	    TRANSFER_transaction
	    signed_transaction
	    fulfillment
	    asset
	}
	
	{
	    generate_keys -> pubkey_alice
	    generate_keys -> privkey_alice
	    generate_keys -> pubkey_bob
	    generate_keys -> privkey_bob
	    pubkey_bob -> generate_condition
	    generate_condition -> condition
	    privkey_alice -> sign
	    CREATE_transaction -> spend
            CREATE_transaction -> get_asset
            get_asset -> asset
	    spend -> fulfillment
	    TRANSFER_transaction -> sign
	    sign -> signed_transaction
	    asset -> transfer
	    fulfillment -> transfer
	    condition -> transfer
	    transfer -> TRANSFER_transaction
	}

	{ rank=same pubkey_alice privkey_alice pubkey_bob privkey_bob }
    }

