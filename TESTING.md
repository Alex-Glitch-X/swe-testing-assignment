# Testing Strategy — Quick-Calc

## Overview

This document describes the testing strategy applied to the Quick-Calc project,
including what was tested, what was intentionally excluded, and how the strategy
maps to the core concepts covered in the course.

---

## What Was Tested and What Was Not

**Tested:**
- All four arithmetic operations via unit tests.
- Edge cases: division by zero, negative operands, decimal results, large numbers.
- Full user interaction workflows via integration tests.

**Not Tested:**
- Non-functional aspects such as performance or memory consumption.
- A graphical user interface was not implemented, so UI rendering is out of scope.

---

## Lecture Concepts Applied

### 1. The Testing Pyramid
The Testing Pyramid prescribes a large base of fast unit tests, a smaller middle
layer of integration tests, and a minimal top layer of end-to-end tests. This
project reflects those proportions: 13 unit tests form the broad base, 3
integration tests form the middle tier, and no UI end-to-end tests are included
as no GUI was built.

### 2. Black-box vs White-box Testing
Unit tests use a **white-box** approach — the internal logic of each method is
known and tests are designed to cover all branches, including the ValueError
raised on division by zero.
Integration tests use a **black-box** approach — they simulate a user providing
inputs and assert on observable outputs without inspecting internal state at
each step.

### 3. Functional vs Non-Functional Testing
All tests in this suite are **functional** — they verify correct outputs for
given inputs. Non-functional testing was deliberately excluded as it falls
outside the scope of a single-user arithmetic utility.

### 4. Regression Testing
The full test suite acts as a regression safety net. Any future modification to
calculator.py can be validated instantly by running pytest. If a change
accidentally breaks the division-by-zero guard, test_division_by_zero_raises_error
will fail immediately, catching the regression before it reaches production.

---

## Test Results Summary

| Test Name                                 | Type        | Status  |
|-------------------------------------------|-------------|---------|
| test_addition_positive_numbers            | Unit        | Pass    |
| test_addition_negative_numbers            | Unit        | Pass    |
| test_addition_with_zero                   | Unit        | Pass    |
| test_subtraction_positive_numbers         | Unit        | Pass    |
| test_subtraction_result_is_negative       | Unit        | Pass    |
| test_multiplication_positive_numbers      | Unit        | Pass    |
| test_multiplication_by_zero               | Unit        | Pass    |
| test_division_positive_numbers            | Unit        | Pass    |
| test_division_decimal_result              | Unit        | Pass    |
| test_division_by_zero_raises_error        | Unit        | Pass    |
| test_addition_large_numbers               | Unit        | Pass    |
| test_multiplication_negative_numbers      | Unit        | Pass    |
| test_clear_resets_result                  | Unit        | Pass    |
| test_full_addition_workflow               | Integration | Pass    |
| test_clear_after_calculation_resets_state | Integration | Pass    |
| test_chained_operations_workflow          | Integration | Pass    |
