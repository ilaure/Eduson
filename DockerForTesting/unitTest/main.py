import pytest


def setup_module(module):
    # init_something()
    pass


def teardown_module(module):
    # teardown_something()
    pass


def test_upper():
    assert 'foo'.upper() == 'FOO'


def test_isupper():
    assert 'FOO'.isupper()


def test_lower():
    assert 'FOO'.lower() == 'fo0'


def test_islower():
    assert 'foo'.islower()
