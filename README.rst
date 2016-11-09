===============================
bdb-transaction-cli
===============================

A minimal command line tool for create and sign BigchainDB transactions.

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
