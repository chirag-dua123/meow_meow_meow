from src import basics, calculator
import pytest

def test_multiply():
    assert basics.multiply(3, 4) == 12

def test_run_calc():
    assert calculator.run_calculator(4, 2, '/') == 2

def test_invalid_operator():
    with pytest.raises(ValueError):
        calculator.run_calculator(1, 2, '%')

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.run_calculator(4, 0, '/')
