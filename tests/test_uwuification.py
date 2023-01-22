"""Test the arts of Uwuification"""

from __future__ import annotations

import pytest

from imsosorry.uwuification import word_replace


@pytest.mark.parametrize(
    "in_text,out_text",
    [
        ("cats are small", "cats are smol"),
        ("I love dogs", "I luv dogs"),
    ],
)
def test_word_replace(in_text: str, out_text: str) -> None:
    assert word_replace(in_text) == out_text
