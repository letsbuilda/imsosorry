"""Regex and map constants for uwuification."""

import re

REGEX_WORD_REPLACE = re.compile(r"(?<!w)[lr](?!w)")
"""A regex that to detect certain characters to change to "w"s."""

REGEX_PUNCTUATION = re.compile(r"[.!?\r\n\t]")
"""A regex to detect certain punctuation characters to emotify /(^•ω•^)"""

REGEX_TILDE = re.compile(r"(?![^ ])(?<!\B)")
"""A regex to find places to add tildes (~) to."""

REGEX_STUTTER = re.compile(r"(\s)([a-zA-Z])")
"""A regex to find words to stutter."""

REGEX_NYA = re.compile(r"n([aeou][^aeiou])")
"""A regex to detect words with an n before a vowel to nyaify."""
SUBSTITUTE_NYA = r"ny\1"
"""A regex to to nyaify words."""

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
