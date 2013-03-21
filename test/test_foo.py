import sys


def test_fail_on_26():
    assert sys.version_info[:2] != (2, 6)


def test_always_pass():
    assert True
