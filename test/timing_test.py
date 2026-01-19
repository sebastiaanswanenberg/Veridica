"Testing the timed decorator."

import os
import sys
import time
import pytest

from veridica.timing import timed

# ensure src/ is importable when running tests directly (avoids relative import errors)
_pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_src_path = os.path.join(_pkg_root, "src")
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)


def test_timed_returns_elapsed_and_result():
    """Test that the timed decorator returns elapsed time and function result."""

    @timed
    def add(a, b):
        """Adds two numbers."""
        return a + b

    elapsed, result = add(2, 3)
    assert result == 5
    assert isinstance(elapsed, float)
    assert elapsed < 1.0


def test_timed_with_sleep_still_reports_elapsed_less_than_one_second():
    """Test that a function with a sleep still returns elapsed time less than one second."""

    @timed
    def sleepy():
        time.sleep(0.05)
        return "done"

    elapsed, result = sleepy()
    assert result == "done"
    assert elapsed < 1.0


def test_timed_preserves_metadata():
    """Test that the timed decorator preserves function metadata like name and docstring."""

    @timed
    def foo2323():
        "example doc"
        return None

    # wrapper should preserve name and docstring via functools.wraps
    assert foo2323.__name__ == "foo2323"
    assert foo2323.__doc__ == "example doc"


def test_timed_propagates_exceptions():
    """Test that exceptions raised in the decorated function are propagated correctly."""

    @timed
    def bad():
        raise ValueError("oops")

    with pytest.raises(ValueError):
        bad()
