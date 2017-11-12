#! venv/bin/python

from sample import square
import pytest

def test_square_with_positive_input():
    assert square(3) == 9

def test_square_with_negative_input():
    assert square(-4) == 16

def test_square_with_zero():
    assert square(0) == 0

def test_square_with_a_string():
    with pytest.raises(TypeError):
        assert square("s")
