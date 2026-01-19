" Test suite for the levenshtein_distance function in batch mode. "

import os
import sys

from veridica.similarity import levenshtein_distance
from veridica.batch import compare_many

# ensure src/ is importable when running tests directly (avoids relative import errors)
_pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_src_path = os.path.join(_pkg_root, "src")
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)


def test_compare_one_to_many_list():
    "Test comparing one target string to many candidates using levenshtein_distance."

    target = "Given I have 5 cucumbers"
    candidates = [
        "Given I have five cucumbers",
        "When I press the button",
        "Given I have 5 cucumbers",
    ]
    results = list(compare_many(target, candidates, levenshtein_distance))

    expected = sorted(
        [(c, levenshtein_distance(target, c)) for c in candidates],
        key=lambda item: item[1],
        reverse=True,
    )
    assert results == expected


def test_compare_one_to_many_generator():
    "Test comparing target string to many candidates using ld with a generator."
    target = "abc"
    candidates_seq = (s for s in ["", "a", "ab"])
    results = list(compare_many(target, candidates_seq, levenshtein_distance))
    expected = sorted(
        [(c, levenshtein_distance(target, c)) for c in ["", "a", "ab"]],
        key=lambda item: item[1],
        reverse=True,
    )
    assert results == expected


def test_compare_one_to_many_empty():
    "Test comparing one target string to an empty list of candidates."

    target = "anything"
    candidates = []
    results = list(compare_many(target, candidates, levenshtein_distance))
    assert not results
