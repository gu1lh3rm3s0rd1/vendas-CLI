"""Make the `tests` directory a package so test modules can be run with -m.

This lets you run a single test module like:

    python -m tests.test_parser

instead of invoking the test file directly.
"""

__all__ = ["test_parser", "test_report", "test_output"]
