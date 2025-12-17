from src import calculator
import pytest

def test_check_float():
    assert calculator.check_float(3.14) == True
    assert calculator.check_float(-0.001) == True
    with pytest.raises(ValueError):
        calculator.check_float("not a float")