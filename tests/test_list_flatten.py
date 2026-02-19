"""Tests for list-flatten."""

import pytest
from list_flatten import flatten


class TestFlatten:
    """Test suite for flatten."""

    def test_basic(self):
        """Test basic usage."""
        result = flatten("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            flatten("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = flatten(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
