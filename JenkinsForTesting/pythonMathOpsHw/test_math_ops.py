import pytest
from math_ops import *


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(2, 3) == 4


def test_divide():
    assert divide(10, 5) == 2


class TestCase(object):
    @pytest.mark.parametrize("test_input,expected", [
        ("3+5", 8),
        ("5+5", 10),
        ("2+4", 6),
        ("6*9", 54),
        ("5*5", 25),
        ("50-10", 40),
        ("100-10", 90),
        ("0-0", 1),
        ("4-2", 2),
    ])
    def tests_in_testCase(self, test_input, expected):
        assert eval(test_input) == expected
