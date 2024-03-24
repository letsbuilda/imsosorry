"""Uwuification of text."""

from __future__ import annotations

import random
from copy import copy
from functools import partial

from imsosorry.uwuification.replacers.regex import re_sub, re_sub_maybe

from .constants import (
    EMOJIS,
    REGEX_NYA,
    REGEX_PUNCTUATION,
    REGEX_STUTTER,
    REGEX_TILDE,
    REGEX_WORD_REPLACE,
    SUBSTITUTE_NYA,
    WORD_REPLACE,
)


def stutter_string(text: str) -> str:
    """Repeat the last character in a string."""
    return f"{text}-{text[-1]}"


def emoji_string(_text: str) -> str:
    """Return a random emoji."""
    return f" {random.choice(EMOJIS)} "


def word_replace(text: str) -> str:
    """Replace words that are keys in the word replacement hash to the values specified."""
    for word, replacement in WORD_REPLACE.items():
        text = text.replace(word, replacement)
    return text


def nyaify(text: str) -> str:
    """Nyaify a string by adding a 'y' between an 'n' and a vowel."""
    return re_sub(text=text, match_pattern=REGEX_NYA, replace_pattern=SUBSTITUTE_NYA)


def char_replace(text: str) -> str:
    """Replace certain characters with 'w'."""
    return re_sub(text=text, match_pattern=REGEX_WORD_REPLACE, replace_pattern="w")


def stutter(text: str, strength: float) -> str:
    """Add stuttering to a string."""
    return re_sub_maybe(text=text, pattern=REGEX_STUTTER, text_getter=stutter_string, strength=strength)


def emoji(text: str, strength: float) -> str:
    """Replace some punctuation with emoticons."""
    return re_sub_maybe(text=text, pattern=REGEX_PUNCTUATION, text_getter=emoji_string, strength=strength)


def tildify(text: str, strength: float) -> str:
    """Add some tildes to spaces."""
    return re_sub_maybe(text=text, pattern=REGEX_TILDE, text_getter=lambda _text: "~", strength=strength)


def uwuify(
    text: str,
    *,
    stutter_strength: float = 0.2,
    emoji_strength: float = 0.1,
    tilde_strength: float = 0.1,
    minimun_processable_length: int = 2,
) -> str:
    """Uwuify a string."""
    contains_alpha = any(char.isalpha() for char in text)

    if len(text) < minimun_processable_length and not contains_alpha:
        return random.choice(EMOJIS)

    text = text.lower()
    original_text = copy(text)

    transforms = [
        word_replace,
        nyaify,
        char_replace,
        stutter,
        partial(stutter, strength=stutter_strength),
        partial(emoji, strength=emoji_strength),
        partial(tildify, strength=tilde_strength),
    ]
    for transform in transforms:
        text = transform(text)  # type: ignore[operator]

    if text == original_text and contains_alpha:
        return uwuify(
            text,
            stutter_strength=stutter_strength + 0.225,
            emoji_strength=emoji_strength + 0.075,
            tilde_strength=tilde_strength + 0.175,
        )

    return text
