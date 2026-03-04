import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_addition_positive_numbers(calc):
    assert calc.add(5, 3) == 8

def test_addition_negative_numbers(calc):
    assert calc.add(-4, -6) == -10

def test_addition_with_zero(calc):
    assert calc.add(0, 99) == 99

def test_subtraction_positive_numbers(calc):
    assert calc.subtract(10, 4) == 6

def test_subtraction_result_is_negative(calc):
    assert calc.subtract(3, 10) == -7

def test_multiplication_positive_numbers(calc):
    assert calc.multiply(6, 7) == 42

def test_multiplication_by_zero(calc):
    assert calc.multiply(100, 0) == 0

def test_division_positive_numbers(calc):
    assert calc.divide(10, 2) == 5.0

def test_division_decimal_result(calc):
    assert calc.divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

def test_division_by_zero_raises_error(calc):
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        calc.divide(9, 0)

def test_addition_large_numbers(calc):
    assert calc.add(999999999, 1) == 1000000000

def test_multiplication_negative_numbers(calc):
    assert calc.multiply(-3, -5) == 15

def test_clear_resets_result(calc):
    calc.result = 42
    calc.current_input = 7
    assert calc.clear() == 0
