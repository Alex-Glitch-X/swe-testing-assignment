# Quick-Calc

Quick-Calc is a lightweight command-line calculator built in Python. It supports addition, subtraction, multiplication, and division, along with a clear/reset function. The project demonstrates a professional Git workflow with a multi-layered automated testing strategy using pytest.

---

## Setup Instructions

**Prerequisites:** Python 3.9 or higher must be installed.

1. Clone the repository:

```bash
git clone https://github.com/Alex-Glitch-X/swe-testing-assignment.git
cd swe-testing-assignment
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run Tests

Run the full test suite with a single command:

```bash
pytest -v
```

Expected output: **16 passed**

---

## Supported Operations

| Operation | Example |
|---|---|
| Addition | 5 + 3 = 8 |
| Subtraction | 10 − 4 = 6 |
| Multiplication | 6 × 7 = 42 |
| Division | 10 ÷ 2 = 5 |
| Clear | Resets result to 0 |

---

## Testing Framework Research: Pytest vs Unittest

Python's standard library includes `unittest`, a class-based testing framework modelled after Java's JUnit. It requires developers to subclass `unittest.TestCase` and use specific assertion methods like `assertEqual` and `assertRaises`. While reliable and dependency-free, the verbosity of defining classes for every test group makes it feel heavyweight for small, focused projects.

`pytest` is a third-party framework where each plain Python function prefixed with `test_` is automatically discovered and run as a test. Its minimal boilerplate, powerful `assert` introspection, and fixture system produce far more readable code. When an assertion fails, pytest displays the actual vs. expected values inline — unittest simply states the test failed without this detail.

For this project, **pytest** was chosen because its readability and fixture support make the test suite easier to maintain and extend. It is the industry-standard choice for modern Python projects. The only trade-off is the external dependency, which is trivially managed via `requirements.txt`.

---

## Project Structure

```
swe-testing-assignment/
├── calculator.py
├── requirements.txt
├── README.md
├── TESTING.md
└── tests/
    ├── __init__.py
    ├── test_unit.py
    └── test_integration.py
```
