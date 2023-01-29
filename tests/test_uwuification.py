"""Test the arts of Uwuification"""

from __future__ import annotations

import pytest

from imsosorry.uwuification import EMOJIS, emoji, word_replace


@pytest.mark.parametrize(
    "in_text,out_text",
    [
        ("cats are small", "cats are smol"),
        ("I love dogs", "I luv dogs"),
    ],
)
def test_word_replace(in_text: str, out_text: str) -> None:
    assert word_replace(in_text) == out_text


@pytest.mark.parametrize(
    "strength,has_emoji",
    [
        (0.0, False),
        (1.0, True),
    ],
)
def test_emoji(strength: float, has_emoji: bool) -> None:
    output = emoji("I love dogs!", strength)
    assert any(emoji_ in output for emoji_ in EMOJIS) == has_emoji
