#! venv/bin/python
from sample import square
import pytest

@pytest.mark.parametrize("number", [3, 4, 5])
def test_square_by_parametrize(number):  
    assert square(number) == number**2