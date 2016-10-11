#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bdb_transaction_cli
----------------------------------

Tests for `bdb_transaction_cli` module.
"""

from click.testing import CliRunner

from bdb_transaction_cli import cli


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert result.output.startswith('Usage:')
