**Warning: This tool is no longer being actively maintained and may not work.**


===============================
bdb-transaction-cli
===============================

A minimal command line tool to create and sign BigchainDB transactions.

* Free software: Apache Software License 2.0
* Documentation: https://docs.bigchaindb.com/projects/cli/en/latest/


Installation
------------

In the shell:

.. code:: shell

  # Checkout the project
  git clone https://github.com/bigchaindb/bdb-transaction-cli/
  cd bdb-transaction-cli

  # Create python virtual environment and install requirements
  virtualenv -p `which python3` .env
  . .env/bin/activate
  pip install -r requirements_dev.txt

  # Install the `bdb` executable into the virtual environment
  python setup.py develop



Features
--------

* Create `CREATE` transactions
* Create `TRANSFER` transactions
* Sign transactions
* Generate key pairs
