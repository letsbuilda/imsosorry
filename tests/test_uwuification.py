"""Test the arts of Uwuification."""

from __future__ import annotations

import pytest

from imsosorry.uwuification import EMOJIS, char_replace, emoji, nyaify, stutter, tildify, uwuify, word_replace


@pytest.mark.parametrize(
    ("in_text", "out_text"),
    [
        ("cats are small", "cats are smol"),
        ("I love dogs", "I luv dogs"),
    ],
)
def test_word_replace(in_text: str, out_text: str) -> None:
    """Test replacing words in text."""
    assert word_replace(in_text) == out_text


@pytest.mark.parametrize(
    ("in_text", "out_text"),
    [
        ("look", "wook"),
        ("rook", "wook"),
        ("wrong", "wrong"),
        ("lr", "ww"),
        ("rl", "ww"),
        ("wrl", "wrw"),
        ("rlw", "wlw"),
        ("wrlw", "wrlw"),
    ],
)
def test_char_replace(in_text: str, out_text: str) -> None:
    """Test replacing characters in text."""
    assert char_replace(in_text) == out_text


@pytest.mark.parametrize(
    ("strength", "in_text", "out_text"),
    [
        (0.0, "cats are small", "cats are small"),
        (1.0, "I love dogs", "I l-love d-dogs"),
    ],
)
def test_stutter(strength: float, in_text: str, out_text: str) -> None:
    """Test adding stutters to text."""
    assert stutter(in_text, strength) == out_text


@pytest.mark.parametrize(
    ("in_text", "out_text"),
    [
        ("naa", "naa"),
        ("nan", "nyan"),
    ],
)
def test_nyaify(in_text: str, out_text: str) -> None:
    """Test nyaifying text."""
    assert nyaify(in_text) == out_text


@pytest.mark.parametrize(
    ("strength", "has_emoji"),
    [
        (0.0, False),
        (1.0, True),
    ],
)
def test_emoji(strength: float, has_emoji: bool) -> None:  # noqa: FBT001 - yes
    """Test adding emojis."""
    output = emoji("I love dogs!", strength)
    assert any(emoji_ in output for emoji_ in EMOJIS) == has_emoji


@pytest.mark.parametrize(
    ("strength", "in_text", "out_text"),
    [
        (0.0, "cats are small", "cats are small"),
        (1.0, "I love dogs", "I~ love~ dogs~"),
    ],
)
def test_tildify(strength: float, in_text: str, out_text: str) -> None:
    """Test adding tildes."""
    assert tildify(in_text, strength) == out_text


@pytest.mark.parametrize(
    "text",
    [
        "-",
        "^",
        ")",
    ],
)
def test_recursion(text: str) -> None:
    """Check that recursion doesn't cause an infinite loop."""
    assert uwuify(text) in EMOJIS
