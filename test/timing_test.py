import os
import sys
import time
import pytest

# ensure src/ is importable when running tests directly (avoids relative import errors)
_pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_src_path = os.path.join(_pkg_root, "src")
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)

from veridica.timing import timed

def test_timed_returns_elapsed_and_result():
    @timed
    def add(a, b):
        """Adds two numbers."""
        return a + b

    elapsed, result = add(2, 3)
    assert result == 5
    assert isinstance(elapsed, float)
    assert elapsed < 1.0

def test_timed_with_sleep_still_reports_elapsed_less_than_one_second():
    @timed
    def sleepy():
        time.sleep(0.05)
        return "done"

    elapsed, result = sleepy()
    assert result == "done"
    assert elapsed < 1.0

def test_timed_preserves_metadata():
    @timed
    def foo():
        "example doc"
        return None

    # wrapper should preserve name and docstring via functools.wraps
    assert foo.__name__ == "foo"
    assert foo.__doc__ == "example doc"

def test_timed_propagates_exceptions():
    @timed
    def bad():
        raise ValueError("oops")

    with pytest.raises(ValueError):
        bad()