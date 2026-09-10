# -*- coding: utf-8 -*-
"""Unit tests for the LibreTX input validation layer."""
import pytest

from validation import (
    InputFields,
    OutputFields,
    MAX_INPUT_INDEX,
    MAX_BTC,
    validate_hex,
    validate_txid,
    validate_input_index,
    validate_btc_amount,
    validate_output_target,
    validate_privkey_present,
    collect_errors,
    format_errors,
)

VALID_TXID = "a" * 64


def _input(**overrides):
    """A fully valid P2PKH input row, with per-test field overrides."""
    base = dict(
        number=1,
        tx_type="P2PKH",
        txid=VALID_TXID,
        index="0",
        script_pub="76a914" + "00" * 20 + "88ac",
        sequence="ffffffff",
        txin_amount="",
        privkey="cThisIsAKey",
    )
    base.update(overrides)
    return InputFields(**base)


def _output(**overrides):
    base = dict(number=1, amount="0.5", target="mtestaddressplaceholder")
    base.update(overrides)
    return OutputFields(**base)


# --- validate_hex -----------------------------------------------------------
@pytest.mark.parametrize("value", ["02000000", "ffffffff", "00"])
def test_validate_hex_accepts_valid(value):
    assert validate_hex("Version", value) is None


@pytest.mark.parametrize("value", ["", "zz", "abc", "0x10", "gg"])
def test_validate_hex_rejects_invalid(value):
    assert validate_hex("Version", value) is not None


# --- validate_txid ----------------------------------------------------------
def test_validate_txid_accepts_64_hex():
    assert validate_txid("Input #1 TXID", VALID_TXID) is None


def test_validate_txid_flags_empty_as_required():
    msg = validate_txid("Input #1 TXID", "")
    assert msg is not None and "required" in msg.lower()


@pytest.mark.parametrize("value", ["a" * 63, "a" * 65, "z" * 64, "abc"])
def test_validate_txid_rejects_bad(value):
    assert validate_txid("Input #1 TXID", value) is not None


# --- validate_input_index ---------------------------------------------------
@pytest.mark.parametrize("value", ["0", "1", "11", str(MAX_INPUT_INDEX)])
def test_validate_input_index_accepts_whole_numbers(value):
    assert validate_input_index("Input #1 Input Index", value) is None


@pytest.mark.parametrize("value", ["", "abc", "1.5", "-1", str(MAX_INPUT_INDEX + 1)])
def test_validate_input_index_rejects_bad(value):
    assert validate_input_index("Input #1 Input Index", value) is not None


# --- validate_btc_amount ----------------------------------------------------
@pytest.mark.parametrize("value", ["0", "0.001", "1.5", "21000000"])
def test_validate_btc_amount_accepts_decimals(value):
    assert validate_btc_amount("Amount", value) is None


def test_validate_btc_amount_flags_empty_required():
    assert "required" in validate_btc_amount("Amount", "").lower()


def test_validate_btc_amount_rejects_non_numeric():
    assert validate_btc_amount("Amount", "abc") is not None


def test_validate_btc_amount_rejects_negative():
    assert "negative" in validate_btc_amount("Amount", "-1").lower()


def test_validate_btc_amount_rejects_over_cap():
    assert validate_btc_amount("Amount", str(MAX_BTC + 1)) is not None


# --- validate_output_target -------------------------------------------------
@pytest.mark.parametrize("value", ["1abc", "3abc", "mabc", "nabc", "2abc", "bc1abc", "tb1abc"])
def test_validate_output_target_accepts_known_prefixes(value):
    assert validate_output_target("Output #1 Address", value, True) is None


@pytest.mark.parametrize("value", ["asdf", "xyz", "0abc", "hello"])
def test_validate_output_target_rejects_unknown_address(value):
    assert validate_output_target("Output #1 Address", value, True) is not None


def test_validate_output_target_requires_value():
    assert "required" in validate_output_target("Output #1 Address", "", True).lower()


def test_validate_output_target_scriptpub_must_be_hex():
    assert validate_output_target("Output #1 Scriptpub", "nothex", False) is not None
    assert validate_output_target("Output #1 Scriptpub", "0014" + "00" * 20, False) is None


# --- validate_privkey_present ----------------------------------------------
def test_validate_privkey_present():
    assert validate_privkey_present("Input #1 Private Key", "") is not None
    assert validate_privkey_present("Input #1 Private Key", "key") is None


# --- collect_errors ---------------------------------------------------------
def test_collect_errors_valid_single_input_is_empty():
    inputs = [_input()] + [
        InputFields(i, "N/A", "", "", "", "", "", "") for i in range(2, 7)
    ]
    outputs = [_output()]
    assert collect_errors(inputs, outputs, True, "02000000", "01000000") == []


def test_collect_errors_flags_the_reported_crash_scenario():
    # invalid txin amount, input index, txid, amount, and unrecognised address
    bad = _input(
        tx_type="P2WPKH",
        txid="notatxid",
        index="notanumber",
        txin_amount="notanamount",
    )
    inputs = [bad] + [InputFields(i, "N/A", "", "", "", "", "", "") for i in range(2, 7)]
    outputs = [_output(amount="bad", target="garbage")]
    errors = collect_errors(inputs, outputs, True, "", "")
    joined = " ".join(errors).lower()
    assert any("txid" in e.lower() for e in errors)
    assert any("input index" in e.lower() for e in errors)
    assert any("txin amount" in e.lower() for e in errors)
    assert any("output #1 amount" in e.lower() for e in errors)
    assert any("not a recognised bitcoin address" in e.lower() for e in errors)
    assert len(errors) >= 5


def test_collect_errors_requires_an_active_input():
    inputs = [InputFields(i, "N/A", "", "", "", "", "", "") for i in range(1, 7)]
    errors = collect_errors(inputs, [_output()], True, "", "")
    assert any("at least one input" in e.lower() for e in errors)


def test_collect_errors_segwit_requires_txin_amount():
    seg = _input(tx_type="P2WPKH", txin_amount="")
    inputs = [seg] + [InputFields(i, "N/A", "", "", "", "", "", "") for i in range(2, 7)]
    errors = collect_errors(inputs, [_output()], True, "", "")
    assert any("txin amount" in e.lower() and "required" in e.lower() for e in errors)


# --- format_errors ----------------------------------------------------------
def test_format_errors_is_human_readable():
    text = format_errors(["First problem.", "Second problem."])
    assert "Please fix the following" in text
    assert "First problem." in text
    assert "Second problem." in text
    assert "•" in text
