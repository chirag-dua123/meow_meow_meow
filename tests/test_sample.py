import pytest
from src.week_1.exercises.calculator import run_calculator

def test_add():
    assert run_calculator(2, 3, '+') == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        run_calculator(4, 0, '/')
