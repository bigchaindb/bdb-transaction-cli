=====
Usage
=====

Here we demonstrate how Alice can make two transactions,
first to create an asset, and then to transfer it to Bob.

Legend:

.. graphviz::

    digraph LEGEND {
	node [fontname="helvetica"];
        data [label="data" shape=record]
        opt [label="optional data" shape=record style=dashed]
        method [label="CLI method" color=red]
    }


Creating an asset
=================

The below diagram shows how to generate a transaction that creates an
asset.

.. graphviz::

    digraph CREATE {
	size = 10;
	rankdir=LR;
	node [fontname="helvetica"];
	node [color=red]

	{ // Inputs (non processes)
	    node [shape=record]
	    node [color=black]
	    output
	    pubkey_alice
	    privkey_alice
            asset [style=dashed]
            metadata [style=dashed]
	    CREATE_transaction
	    signed_transaction
	}
	
	{
	    pubkey_alice -> generate_output
	    generate_output -> output
	    output -> create
	    pubkey_alice -> create
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
	    output
	    pubkey_alice [fontcolor=grey]
	    privkey_alice
	    pubkey_bob
	    privkey_bob [fontcolor=grey]
	    CREATE_transaction
	    TRANSFER_transaction
	    signed_transaction
	    input
	    asset
	}
	
	{
	    generate_keys -> pubkey_alice
	    generate_keys -> privkey_alice
	    generate_keys -> pubkey_bob
	    generate_keys -> privkey_bob
	    pubkey_bob -> generate_output
	    generate_output -> output
	    privkey_alice -> sign
	    CREATE_transaction -> spend
            CREATE_transaction -> get_asset
            get_asset -> asset
	    spend -> input
	    TRANSFER_transaction -> sign
	    sign -> signed_transaction
	    asset -> transfer
	    input -> transfer
	    output -> transfer
	    transfer -> TRANSFER_transaction
	}

	{ rank=same pubkey_alice privkey_alice pubkey_bob privkey_bob }
    }

