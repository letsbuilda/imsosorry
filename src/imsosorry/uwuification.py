"""The ancient arts of Uwuification"""

import random
import re
from functools import partial


class Uwuified:
    """
    Representation for an uwuified object.
    """

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

    def __init__(self, text, stutter_strength=0.2, emoji_strength=0.1, tilde_strength=0.1):
        self.__original = text
        self.__text = text.lower()
        self.__text = self.word_replace(self.__text)
        self.__text = self.nyaify(self.__text)
        self.__text = self.char_replace(self.__text)
        self.__text = self.stutter(self.__text, stutter_strength)
        self.__text = self.emoji(self.__text, emoji_strength)
        self.__text = self.tildify(self.__text, tilde_strength)

    @property
    def original(self):
        """
        Returns the original value of the uwuified object.
        """
        return self.__original

    def __hash__(self) -> int:
        """
        Returns a hash of the uwuified object.
        """
        return hash(self.__original) + hash(self.__text)

    def __str__(self) -> str:
        """
        Returns a string representation of the uwuified object.
        """
        return self.__text

    def __repr__(self) -> str:
        """
        Returns a representation of the uwuified object.
        """
        return f"<Uwuified text={self.__text!r}>"

    def __eq__(self, other) -> bool:
        """
        Returns whether the uwuified object is equal to another object.
        """
        return self.__text in {other.text, other}

    def __ne__(self, other) -> bool:
        """
        Returns whether the uwuified object is not equal to another object.
        """
        return not self.__eq__(other)

    def __len__(self) -> int:
        """
        Returns the length of the uwuified object.
        """
        return len(self.__text)

    def word_replace(self, text: str) -> str:
        """Replaces words that are keys in the word replacement hash to the values specified."""
        for word, replacement in self.WORD_REPLACE.items():
            text = text.replace(word, replacement)
        return text

    def char_replace(self, text: str) -> str:
        """Replace certain characters with 'w'."""
        return self.REGEX_WORD_REPLACE.sub("w", text)

    def stutter_replace(self, match: re.Match, strength: float = 0.0) -> str:
        """Replaces a single character with a stuttered character."""
        match_string = match.group()
        if random.random() < strength:
            return f"{match_string}-{match_string[-1]}"  # Stutter the last character
        return match_string

    def stutter(self, text: str, strength: float) -> str:
        """Adds stuttering to a string."""
        return self.REGEX_STUTTER.sub(partial(self.stutter_replace, strength=strength), text, 0)

    def nyaify(self, text: str) -> str:
        """Nyaifies a string by adding a 'y' between an 'n' and a vowel."""
        return self.REGEX_NYA.sub(self.SUBSTITUTE_NYA, text, 0)

    def emoji_replace(self, match: re.Match, strength: float = 0.0) -> str:
        """Replaces a punctuation character with an emoticon."""
        match_string = match.group()
        if random.random() < strength:
            return f" {random.choice(self.EMOJIS)} "
        return match_string

    def emoji(self, text: str, strength: float) -> str:
        """Replaces some punctuation with emoticons."""
        return self.REGEX_PUNCTUATION.sub(partial(self.emoji_replace, strength=strength), text, 0)

    def tildes(self, match: re.Match, strength: float = 0.0):
        """Adds some tildes to spaces."""
        match_string = match.group()
        if random.random() < strength:
            return "~"
        return match_string

    def tildify(self, text: str, strength: float) -> str:
        """Adds some tildes to spaces."""
        return self.REGEX_TILDE.sub(partial(self.tildes, strength=strength), text, 0)


def uwuify(
    text: str,
    *,
    stutter_strength: float = 0.2,
    emoji_strength: float = 0.1,
    tilde_strength: float = 0.1,
) -> Uwuified:
    """Takes a string and returns an uwuified version of it."""
    uwuified = Uwuified(text, stutter_strength, emoji_strength, tilde_strength)
    return uwuified
