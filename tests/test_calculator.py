import pytest
from calculator import divide, calculate_average, find_max, get_user_by_id

# --- Tests for divide function (Bug fix and Regression) ---

def test_divide_by_zero_raises_error():
    """Verify that dividing by zero raises a ZeroDivisionError with the correct message."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10, 0)
    assert str(excinfo.value) == "Cannot divide by zero."

    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(-5, 0)
    assert str(excinfo.value) == "Cannot divide by zero."

def test_divide_positive_numbers():
    """Regression test: Ensure division of positive numbers works correctly."""
    assert divide(10, 2) == 5
    assert divide(100, 10) == 10
    assert divide(7, 2) == 3.5

def test_divide_negative_numbers():
    """Regression test: Ensure division involving negative numbers works correctly."""
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5
    assert divide(-7, 2) == -3.5

def test_divide_zero_by_non_zero():
    """Regression test: Ensure division of zero by a non-zero number works correctly."""
    assert divide(0, 5) == 0
    assert divide(0, -5) == 0
    assert divide(0, 0.5) == 0

def test_divide_float_results():
    """Regression test: Ensure division yielding float results works correctly."""
    assert divide(5, 2) == 2.5
    assert divide(1, 3) == pytest.approx(0.3333333333333333)

# --- Regression tests for other functions (ensure no regressions) ---

def test_calculate_average_valid_list():
    """Regression test: Verify calculate_average works for a list of numbers."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([10, 20, 30]) == 20.0
    assert calculate_average([2.5, 3.5]) == 3.0
    assert calculate_average([-1, 1, 0]) == 0.0

def test_calculate_average_empty_list_raises_error():
    """Regression test: Verify calculate_average raises ZeroDivisionError for an empty list."""
    with pytest.raises(ZeroDivisionError):
        calculate_average([])

def test_find_max_positive_numbers():
    """Regression test: Verify find_max works for a list of positive numbers."""
    assert find_max([1, 5, 2, 9, 3]) == 9
    assert find_max([10]) == 10

def test_find_max_negative_numbers():
    """Regression test: Verify find_max works for a list of negative numbers."""
    assert find_max([-1, -5, -2, -9, -3]) == -1
    assert find_max([-10, -20, -5]) == -5

def test_find_max_mixed_numbers():
    """Regression test: Verify find_max works for a list of mixed positive/negative numbers."""
    assert find_max([-1, 5, -2, 9, 0]) == 9
    assert find_max([-100, 0, 10, -50]) == 10

def test_find_max_with_floats():
    """Regression test: Verify find_max works for a list of float numbers."""
    assert find_max([1.1, 5.5, 2.2, 9.9, 3.3]) == 9.9

def test_get_user_by_id_existing_user():
    """Regression test: Verify get_user_by_id returns correct user for existing ID."""
    assert get_user_by_id(1) == "Alice"
    assert get_user_by_id(3) == "Charlie"

def test_get_user_by_id_non_existing_user_raises_error():
    """Regression test: Verify get_user_by_id raises KeyError for non-existing ID."""
    with pytest.raises(KeyError):
        get_user_by_id(99)
    with pytest.raises(KeyError):
        get_user_by_id(0)
