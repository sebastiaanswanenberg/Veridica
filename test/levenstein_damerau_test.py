# content of test_sysexit.py
import os
import sys
import pytest

# ensure src/ is importable when running tests directly (avoids relative import errors)
_pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_src_path = os.path.join(_pkg_root, "src")
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)

from veridica.similarity import damerau_levenshtein_distance

@pytest.mark.parametrize("a,b,expected", [
            ("", "", 0),
            (123, 123, 0),
            ("a", "a", 0),
            ("", "abc", 3),
            ("kitten", "sitting", 3),
            ("flaw", "lawn", 2),
            ("gumbo", "gambol", 2),
            ("book", "back", 2),
            ("ä", "a", 1),
            ("Case", "case", 1),
            ("ab", "ba", 1),
            ("Given I have 5 cucumbers", "Given I have five cucumbers", 4),
            ("When I press the button", "When I click the button", 5),
            ("Then the result should be displayed", "Then the result is displayed", 9),
            ("Given I add 1 item to the cart", "Given I add one item to the cart", 3),
            ("Given I have 5 cucumbers.", "Given I have 5 cucumbers", 1),
            ("Given I have a cucumber", "given I have a cucumber", 1),
        ])

def test_gherkin_pairs_symmetry_and_bounds(a, b, expected):
    d = damerau_levenshtein_distance(a, b)
    # distance should be integer, symmetric, positive for different strings, and bounded by the longer string length
    assert isinstance(d, int)
    assert d == damerau_levenshtein_distance(b, a)
    assert d >= 0
    assert (a != b) == (d > 0)
    assert d <= max(len(str(a)), len(str(b)))
    assert damerau_levenshtein_distance(a, b) == expected

def test_gherkin_identical_sentence_is_zero():
    s = "Given I have 5 cucumbers"
    assert damerau_levenshtein_distance(s, s) == 0

def test_gherkin_trailing_insertion_counts_chars():
    base = "Given I have 5 cucumbers"
    added = " and I give 2 away"
    a = base
    b = base + added
    assert damerau_levenshtein_distance(a, b) == len(added)

def test_levenshtein_long_identical_strings():
    s = "x" * 1000
    assert damerau_levenshtein_distance(s, s) == 0