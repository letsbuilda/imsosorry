"""Regex replacers."""

from __future__ import annotations

import random
from functools import partial
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import re
    from collections.abc import Callable


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

    def inner(match: re.Match[str], strength: float) -> str:
        """Replace text randomly."""
        match_string = match.group()
        if random.random() < strength:
            return text_getter(match_string)
        return match_string

    return pattern.sub(partial(inner, strength=strength), text)
