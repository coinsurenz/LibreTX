# -*- coding: utf-8 -*-
"""Input validation for LibreTX transaction fields.

Pure, UI-agnostic validators. Each validator returns a human-readable error
message when the value is invalid, or ``None`` when it is acceptable, so the GUI
layer can collect every problem and show them together before attempting to
build (and sign) a transaction.

Kept free of any PyQt/Qt imports so it can be unit tested on its own.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

# Bitcoin's fixed supply cap, used as an upper bound for amount fields.
MAX_BTC = 21_000_000
# A prev-output index is packed as a signed 32-bit little-endian integer.
MAX_INPUT_INDEX = 2 ** 31 - 1
# Tx types whose signing requires the input amount (BIP143 sighash).
SEGWIT_TYPES = frozenset({"P2SH-P2wPKH", "P2WPKH", "P2WSH", "P2WSH multisig"})
# Recognised leading characters/prefixes for a Bitcoin address.
_ADDRESS_PREFIXES = ("1", "2", "3", "m", "n", "bc1", "tb1")


@dataclass(frozen=True)
class InputFields:
    """The raw text of one input row, exactly as read from the GUI."""

    number: int          # 1-based row number, used only for messages
    tx_type: str         # selected Tx Type, e.g. "P2PKH" or "N/A"
    txid: str
    index: str
    script_pub: str
    sequence: str
    txin_amount: str
    privkey: str


@dataclass(frozen=True)
class OutputFields:
    """The raw text of one output row, exactly as read from the GUI."""

    number: int          # 1-based row number, used only for messages
    amount: str
    target: str          # address or scriptpubkey depending on output format


def _is_hex(value: str) -> bool:
    """True when value is non-empty, even-length, valid hexadecimal."""
    if value == "" or len(value) % 2 != 0:
        return False
    try:
        bytes.fromhex(value)
    except ValueError:
        return False
    return True


def validate_hex(label: str, value: str) -> Optional[str]:
    """Format check for a required hexadecimal field."""
    if not _is_hex(value):
        return f"{label} must be hexadecimal characters (0-9, a-f)."
    return None


def validate_txid(label: str, value: str) -> Optional[str]:
    """A txid must be exactly 64 hexadecimal characters (32 bytes)."""
    if value == "":
        return f"{label} is required (a 64-character hexadecimal transaction id)."
    if len(value) != 64 or not _is_hex(value):
        return f"{label} must be a 64-character hexadecimal transaction id."
    return None


def validate_input_index(label: str, value: str) -> Optional[str]:
    """A prev-output index must be a whole number in signed 32-bit range."""
    if value == "":
        return f"{label} is required (a whole number, 0 to {MAX_INPUT_INDEX})."
    try:
        index = int(value)
    except ValueError:
        return f"{label} must be a whole number (0 to {MAX_INPUT_INDEX})."
    if index < 0 or index > MAX_INPUT_INDEX:
        return f"{label} must be between 0 and {MAX_INPUT_INDEX}."
    return None


def validate_btc_amount(label: str, value: str) -> Optional[str]:
    """An amount must be a decimal BTC value between 0 and the supply cap."""
    if value == "":
        return f"{label} is required (a decimal amount in BTC)."
    try:
        amount = float(value)
    except ValueError:
        return f"{label} is invalid. Enter a decimal amount in BTC."
    if amount < 0:
        return f"{label} cannot be negative."
    if amount > MAX_BTC:
        return f"{label} cannot exceed {MAX_BTC:,} BTC."
    return None


def validate_output_target(label: str, value: str, is_address: bool) -> Optional[str]:
    """Validate an output target as either an address or a scriptpubkey.

    Address checking is deliberately limited to prefix recognition so that a
    valid address is never wrongly rejected; a bad checksum is caught later by
    the builder's safety net.
    """
    if value == "":
        return f"{label} is required."
    if not is_address:
        if not _is_hex(value):
            return f"{label} must be a hexadecimal scriptpubkey (0-9, a-f)."
        return None
    if not value.startswith(_ADDRESS_PREFIXES):
        return (
            f"{label} is not a recognised Bitcoin address. Expected a legacy "
            "address starting 1, 2, 3, m or n, or a bech32 address starting bc1 or tb1."
        )
    return None


def validate_privkey_present(label: str, value: str) -> Optional[str]:
    """A private key is required to sign an active input."""
    if value == "":
        return f"{label} is required to sign this input."
    return None


def _add(errors: list, message: Optional[str]) -> None:
    if message is not None:
        errors.append(message)


def collect_errors(
    inputs: list,
    outputs: list,
    outputs_are_addresses: bool,
    version: str,
    hashtype: str,
) -> list:
    """Return a list of human-readable errors for the given transaction fields.

    Only active inputs (Tx Type not "N/A") and the supplied active outputs are
    checked. An empty list means the fields passed validation.
    """
    errors: list = []

    active_inputs = [row for row in inputs if row.tx_type != "N/A"]
    if not active_inputs:
        errors.append("Select at least one input Tx Type (all inputs are set to N/A).")

    for row in active_inputs:
        n = row.number
        _add(errors, validate_txid(f"Input #{n} TXID", row.txid))
        _add(errors, validate_input_index(f"Input #{n} Input Index", row.index))
        _add(errors, validate_privkey_present(f"Input #{n} Private Key", row.privkey))
        if row.script_pub != "":
            _add(errors, validate_hex(f"Input #{n} Script pubkey", row.script_pub))
        if row.sequence != "":
            _add(errors, validate_hex(f"Input #{n} Sequence", row.sequence))
        # The txin amount is only used to sign segwit inputs (BIP143 sighash);
        # for non-segwit types the field is unused, so it is not validated.
        if row.tx_type in SEGWIT_TYPES:
            _add(errors, validate_btc_amount(f"Input #{n} Txin Amount", row.txin_amount))

    if not outputs:
        errors.append("Select at least one output (Num Outs).")
    for row in outputs:
        n = row.number
        _add(errors, validate_btc_amount(f"Output #{n} Amount", row.amount))
        target_label = f"Output #{n} " + ("Address" if outputs_are_addresses else "Scriptpub")
        _add(errors, validate_output_target(target_label, row.target, outputs_are_addresses))

    if version != "":
        _add(errors, validate_hex("Version", version))
    if hashtype != "":
        _add(errors, validate_hex("Hash type", hashtype))

    return errors


def format_errors(errors: list) -> str:
    """Render collected errors as a plain-text bulleted block for the output box."""
    header = "Please fix the following before creating a signed transaction:\n"
    return header + "\n".join(f"  • {message}" for message in errors)
