from src import calculator
import pytest

def check_float(a):
    if isinstance(a, float):
        return True
    raise ValueError("Not a float")