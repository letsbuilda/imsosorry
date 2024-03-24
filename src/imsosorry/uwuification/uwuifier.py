"""The ancient arts of Uwuification."""

from __future__ import annotations

import random
from copy import copy
from functools import partial
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import re
    from collections.abc import Callable

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


def word_replace(text: str) -> str:
    """Replace words that are keys in the word replacement hash to the values specified."""
    for word, replacement in WORD_REPLACE.items():
        text = text.replace(word, replacement)
    return text


def stutter_string(text: str) -> str:
    """Repeat the last character in a string."""
    return f"{text}-{text[-1]}"


def emoji_string(_text: str) -> str:
    """Return a random emoji."""
    return f" {random.choice(EMOJIS)} "


def re_sub(
    text: str,
    match_pattern: re.Pattern[str],
    replace_pattern: str,
) -> str:
    """Replace pattern in string."""
    return match_pattern.sub(replace_pattern, text)


def re_sub_maybe(
    text: str,
    pattern: re.Pattern[str],
    text_getter: Callable[[str], str],
    strength: float = 0.0,
) -> str:
    """Replace pattern in string randomly."""
    matches = pattern.findall(text)
    for match in matches:
        new_text = match.group()
        if random.random() < strength:
            new_text = text_getter(new_text)
        text = text.replace(match, new_text)
    return text


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
        partial(re_sub, match_pattern=REGEX_NYA, replace_pattern=SUBSTITUTE_NYA),
        partial(re_sub, match_pattern=REGEX_WORD_REPLACE, replace_pattern="w"),
        partial(re_sub_maybe, pattern=REGEX_STUTTER, text_getter=stutter_string, strength=stutter_strength),
        partial(re_sub_maybe, pattern=REGEX_PUNCTUATION, text_getter=emoji_string, strength=emoji_strength),
        partial(re_sub_maybe, pattern=REGEX_TILDE, text_getter=lambda _text: "~", strength=tilde_strength),
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
