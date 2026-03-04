import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_full_addition_workflow(calc):
    first_operand = 5
    operator = "+"
    second_operand = 3
    if operator == "+":
        calc.result = calc.add(first_operand, second_operand)
    assert calc.result == 8

def test_clear_after_calculation_resets_state(calc):
    calc.result = calc.divide(20, 4)
    assert calc.result == 5.0
    calc.clear()
    assert calc.result == 0
    assert calc.current_input == 0

def test_chained_operations_workflow(calc):
    intermediate = calc.subtract(10, 3)
    final = calc.multiply(intermediate, 2)
    assert final == 14
