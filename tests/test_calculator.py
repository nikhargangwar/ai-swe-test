import pytest
from calculator import divide, calculate_average, find_max, get_user_by_id

# Tests for the divide function
def test_divide_positive_numbers():
    """Tests division with two positive numbers."""
    assert divide(10, 2) == 5

def test_divide_negative_numbers():
    """Tests division with two negative numbers."""
    assert divide(-10, -2) == 5

def test_divide_positive_and_negative():
    """Tests division with a positive and a negative number."""
    assert divide(10, -2) == -5
    assert divide(-10, 2) == -5

def test_divide_float_result():
    """Tests division that results in a float."""
    assert divide(5, 2) == 2.5

def test_divide_by_zero_raises_error():
    """Tests that dividing by zero raises a ZeroDivisionError with a specific message."""
    with pytest.raises(ZeroDivisionError, match='Division by zero is not allowed.'):
        divide(10, 0)

def test_divide_zero_by_number():
    """Tests dividing zero by a non-zero number."""
    assert divide(0, 5) == 0

# Tests for calculate_average (ensure no regression)
def test_calculate_average_basic():
    """Tests basic functionality of calculate_average."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_calculate_average_empty_list():
    """Tests calculate_average with an empty list (should raise ZeroDivisionError)."""
    with pytest.raises(ZeroDivisionError):
        calculate_average([])

def test_calculate_average_single_element():
    """Tests calculate_average with a single element."""
    assert calculate_average([10]) == 10

def test_calculate_average_negative_numbers():
    """Tests calculate_average with negative numbers."""
    assert calculate_average([-1, -2, -3]) == -2

# Tests for find_max (ensure no regression)
def test_find_max_basic():
    """Tests basic functionality of find_max."""
    assert find_max([1, 5, 3, 9, 2]) == 9

def test_find_max_negative_numbers():
    """Tests find_max with negative numbers."""
    assert find_max([-1, -5, -3, -9, -2]) == -1

def test_find_max_mixed_numbers():
    """Tests find_max with mixed positive and negative numbers."""
    assert find_max([-1, 5, -3, 9, 0]) == 9

def test_find_max_single_element():
    """Tests find_max with a single element."""
    assert find_max([7]) == 7

def test_find_max_duplicate_max():
    """Tests find_max when the maximum value appears multiple times."""
    assert find_max([1, 5, 9, 3, 9, 2]) == 9

# Tests for get_user_by_id (ensure no regression)
def test_get_user_by_id_existing():
    """Tests get_user_by_id for an existing user."""
    assert get_user_by_id(1) == "Alice"
    assert get_user_by_id(2) == "Bob"

def test_get_user_by_id_non_existing():
    """Tests get_user_by_id for a non-existing user (should raise KeyError)."""
    with pytest.raises(KeyError):
        get_user_by_id(4)

def test_get_user_by_id_zero_id():
    """Tests get_user_by_id with an ID of 0 (should raise KeyError)."""
    with pytest.raises(KeyError):
        get_user_by_id(0)
