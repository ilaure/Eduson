import pytest
from ops import *


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 5) == 1


class TestCase(object):
    @pytest.mark.parametrize("test_input,expected", [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 42),
    ])
    def tests_in_testCase(self, test_input, expected):
        assert eval(test_input) == expected
