"""Test suite for number normalisation functions in veridica.normalisation."""

import os
import sys
from veridica.normalisation import min_max_normalize
from veridica.similarity import levenshtein_distance
from veridica.batch import compare_many

# ensure src/ is importable when running tests directly (avoids relative import errors)
_pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_src_path = os.path.join(_pkg_root, "src")
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)


def test_compare_one_to_many_list():
    "Test comparing one target string to many candidates using levenshtein_distance. and see if all values are between 1.0 and 0.0"

    target = "Given I have 5 cucumbers"
    candidates = [
        "Given I have five cucumbers",
        "When I press the button",
        "Given I have 5 cucumbers",
    ]
    results = list(min_max_normalize(compare_many(target, candidates, levenshtein_distance)))

    assert all(item[1] >= 0.0 for item in results)
    assert all(item[1] <= 1.0 for item in results)
