"""The ancient arts of Uwuification"""

from __future__ import annotations

import random
import re
from typing import Callable

_WORD_REPLACE = {
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

_EMOJIS = [
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
    "(U ﹏ U)",
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
    "(ˆ ﻌ ˆ)♡",
    "^•ﻌ•^",
    "/(^•ω•^)",
    "(✿oωo)",
]
"""A list of emojis/emoticons to add."""


Dice = Callable[[], bool]


def random_dice(strength: float) -> Dice:
    return lambda: random.random() < strength


def uwuify(
    text: str,
    *,
    stutter: Dice = random_dice(0.2),
    emojis: Dice = random_dice(0.1),
    tilde: Dice = random_dice(0.1),
) -> str:
    text = text.lower()

    for word, replacement in _WORD_REPLACE.items():
        text = text.replace(word, replacement)

    pattern: str
    for pattern, replacer in [
        # name -> nyame
        (r"n([aeou][^aeiou])", r"ny\1"),

        # crabs crawl -> cwabs cwawl
        (r"(?<!w)[lr](?!w)", "w"),

        # stutter some words:
        # a nice kitten -> a n-nice k-kitten
        (r"(\s)([a-zA-Z])", lambda s: f"{s[0]}-{s[2]}" if stutter() else s[0]),

        # w-why not spwinkwe in some emojis (owo)
        # would y-you go out with me? -> would y-you go out with me >w<
        (r"[.!?\n]", lambda s: f" {random.choice(_EMOJIS)} " if emojis() else s[0]),

        # add a tilde at the end of some words:
        # hewwo wowld nifty-fifty! uwu -> hewwo~ wowld~ nifty-fifty! uwu~
        (r"\b(?=\s|$)", lambda _: "~" if tilde() else ""),
    ]:
        text = re.sub(pattern, replacer, text)

    return text
