"""The ancient arts of Uwuification."""

from __future__ import annotations

import random
import re
from copy import copy
from functools import partial
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

WORD_REPLACE = {
    "small": "smol",
    "cute": "kawaii~",
    "fluff": "floof",
    "love": "luv",
    "stupid": "baka",
    "idiot": "baka",
    "what": "nani",
    "meow": "nya~",
    "roar": "rawrr~",
}
"""A dict to match certain words for replacement words"""

EMOJIS = [
    "rawr x3",
    "OwO",
    "UwU",
    "o.O",
    "-.-",
    ">w<",
    "(⑅˘꒳˘)",
    "(ꈍᴗꈍ)",
    "(˘ω˘)",
    "(U ᵕ U❁)",
    "σωσ",
    "òωó",
    "(///ˬ///✿)",
    "(U ﹏ U)",  # noqa: RUF001 - literally the point...
    "( ͡o ω ͡o )",
    "ʘwʘ",
    ":3",
    ":3",  # important enough to have twice
    "XD",
    "nyaa~~",
    "mya",
    ">_<",
    "😳",
    "🥺",
    "😳😳😳",
    "rawr",
    "^^",
    "^^;;",
    "(ˆ ﻌ ˆ)♡",  # noqa: RUF001 - literally the point...
    "^•ﻌ•^",
    "/(^•ω•^)",
    "(✿oωo)",
]
"""A list of emojis/emoticons to add."""

REGEX_WORD_REPLACE = re.compile(r"(?<!w)[lr](?!w)")
"""A regex that to detect certain characters to change to "w"s."""

REGEX_PUNCTUATION = re.compile(r"[.!?\r\n\t]")
"""A regex to detect certain punctuation characters to emotify /(^•ω•^)"""

REGEX_TILDE = re.compile(r"(?![^ ])(?<!\B)")
"""A regex to find places to add tildes (~) to."""

REGEX_STUTTER = re.compile(r"(\s)([a-zA-Z])")
"""A regex to find words to stutter."""
SUBSTITUTE_STUTTER = r"\g<1>\g<2>-\g<2>"
"""A regex to add st-stuttering to strings."""

REGEX_NYA = re.compile(r"n([aeou][^aeiou])")
"""A regex to detect words with an n before a vowel to nyaify."""
SUBSTITUTE_NYA = r"ny\1"
"""A regex to to nyaify words."""


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
        partial(re_sub_maybe, pattern=REGEX_TILDE, text_getter=stutter_string, strength=stutter_strength),
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
