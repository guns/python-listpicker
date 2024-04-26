"""
Interactive list selection with filtering.

    listpicker.pick("Choose pizza type:", ("Thin crust", …))
    listpicker.pick_multiple("Choose toppings:", ("Pepperoni", …))
"""

import sys
from typing import Optional, Sequence, TextIO

from .listpicker import ListPicker

__all__ = ("pick", "pick_multiple")


def pick(
    prompt: str,
    options: Sequence[str],
    *,
    force_prompt: bool = False,
    infile: TextIO = sys.stdin,
    outfile: TextIO = sys.stdout,
) -> Optional[str]:
    """
    Prompt user to choose one option from many. If "options" is empty, returns
    None without prompting. Similarly, if "options" has one element, that
    element is returned without prompting the user. Pass force_prompt=True to
    always prompt the user when len(options) == 1.
    """
    if len(options) == 0:
        return None

    if len(options) == 1 and not force_prompt:
        return options[0]

    if picks := ListPicker(prompt, options, infile=infile, outfile=outfile).pick():
        return picks[0]

    return None


def pick_multiple(
    prompt: str,
    options: Sequence[str],
    *,
    force_prompt: bool = False,
    minimum: int = 1,
    infile: TextIO = sys.stdin,
    outfile: TextIO = sys.stdout,
) -> list[str]:
    """
    Prompt user to select a subset of "options". If len(options) <= minimum,
    the same options are returned in a new list without prompting the user.
    Pass force_prompt=True to always prompt the user when len(options) == minimum.

    This function always returns a new list that contains a subsequence of
    "options" (i.e. same ordering).
    """
    if len(options) < minimum or len(options) == minimum and not force_prompt:
        return list(options)

    return ListPicker(prompt, options, multiselect=True, minimum=minimum, infile=infile, outfile=outfile).pick()
