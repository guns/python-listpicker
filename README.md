python-listpicker
=================

Interactive list selection for POSIX terminals.

Python 3.10+

Features
--------

- Single and multiple selection from a list of strings
- Interactive substring filtering
- Paging for long lists
- Common navigation keybindings (vi, emacs, arrow keys, Home/End, etc)
- Direct terminal manipulation with CSI commands (i.e. no curses)
- Draw to main screen buffer without clearing the screen
- Proper truncation of long lines with SGR color sequences
- Redraw on terminal resize (SIGWINCH)
- Help menu and multiselect confirmation prompt

Screenshots
-----------

Examples
--------

### Basic usage

```python
import listpicker

pizza_styles = ("Thin crust", "Stuffed crust", "Deep dish")
style = listpicker.pick("Choose pizza style:", pizza_styles)

# User can abort input, so handle the case where "pick()" returns "None"
if style is None:
    style = pizza_styles[0]

pizza_toppings = ("Pepperoni", "Sausage", "Mushroom", "Pineapple")
toppings = listpicker.pick_multiple("Choose toppings:", pizza_toppings)
```

### Typical usage with dictionary

```python
import dataclasses

import listpicker


@dataclasses.dataclass
class Book:
    isbn: str
    title: str
    authors: list[str]
    publication_year: int


books = [
    Book(
        "0201038013",
        "The Art of Computer Programming, Volume 1: Fundamental Algorithms",
        ["Knuth, Donald"],
        1968,
    ),
    Book(
        "0262010771",
        "Structure and Interpretation of Computer Programs",
        ["Harold Abelson", "Gerald Jay Sussman", "Julie Sussman"],
        1984,
    ),
    Book(
        "032163537X",
        "Elements of Programming",
        ["Stepanov, Alexander A.", "McJones, Paul"],
        2009,
    ),
]

options = {f"{b.title} ({b.publication_year})": b for b in books}
choice = listpicker.pick("Pick a book:", list(options.keys()))

# Pick a book:
#   (filter with f, submit with Enter, F1 for keybindings)
# > 1. The Art of Computer Programming, Volume 1: Fundamental Algorithms (1968)
#   2. Structure and Interpretation of Computer Programs (1984)
#   3. Elements of Programming (2009)

if choice:
    book = options[choice]
```
