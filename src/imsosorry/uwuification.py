"""The ancient arts of Uwuification."""

from __future__ import annotations

import random
import re
from functools import partial

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
"""A wegex that to detect certain characters to change to "w"s."""

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


def char_replace(text: str) -> str:
    """Replace certain characters with 'w'."""
    return REGEX_WORD_REPLACE.sub("w", text)


def stutter_replace(match: re.Match, strength: float = 0.0) -> str:
    """Replace a single character with a stuttered character."""
    match_string = match.group()
    if random.random() < strength:
        return f"{match_string}-{match_string[-1]}"  # Stutter the last character
    return match_string


def stutter(text: str, strength: float) -> str:
    """Add stuttering to a string."""
    return REGEX_STUTTER.sub(partial(stutter_replace, strength=strength), text, 0)


def nyaify(text: str) -> str:
    """Nyaify a string by adding a 'y' between an 'n' and a vowel."""
    return REGEX_NYA.sub(SUBSTITUTE_NYA, text, 0)


def emoji_replace(match: re.Match, strength: float = 0.0) -> str:
    """Replace a punctuation character with an emoticon."""
    match_string = match.group()
    if random.random() < strength:
        return f" {random.choice(EMOJIS)} "
    return match_string


def emoji(text: str, strength: float) -> str:
    """Replace some punctuation with emoticons."""
    return REGEX_PUNCTUATION.sub(partial(emoji_replace, strength=strength), text, 0)


def tildes(match: re.Match, strength: float = 0.0) -> str:
    """Add some tildes to spaces."""
    match_string = match.group()
    if random.random() < strength:
        return "~"
    return match_string


def tildify(text: str, strength: float) -> str:
    """Add some tildes to spaces."""
    return REGEX_TILDE.sub(partial(tildes, strength=strength), text, 0)


def uwuify(
    text: str,
    *,
    stutter_strength: float = 0.2,
    emoji_strength: float = 0.1,
    tilde_strength: float = 0.1,
) -> str:
    """Take a string and returns an uwuified version of it."""
    text = text.lower()
    text = word_replace(text)
    text = nyaify(text)
    text = char_replace(text)
    text = stutter(text, stutter_strength)
    text = emoji(text, emoji_strength)
    return tildify(text, tilde_strength)
