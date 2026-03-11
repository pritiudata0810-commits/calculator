"""Pytest configuration file that creates test structure if needed."""
import os
import sys

# Import the test initializer module to ensure structure is created
try:
    import test_init
except ImportError:
    pass

# Ensure tests directory exists (in same directory as this file)
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
tests_dir = os.path.abspath(tests_dir)

if not os.path.exists(tests_dir):
    os.makedirs(tests_dir, exist_ok=True)
    
# Ensure __init__.py exists
init_file = os.path.join(tests_dir, '__init__.py')
if not os.path.exists(init_file):
    open(init_file, 'a').close()

# Create test_calculator.py if it doesn't exist
test_file = os.path.join(tests_dir, 'test_calculator.py')
if not os.path.exists(test_file):
    test_content = '''"""
Unit tests for the calculator module.
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestBasicOperations:
    """Test basic arithmetic operations."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5
        assert add(0, 5) == 5
        assert add(100, 50) == 150

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-2, 3) == 1
        assert add(-5, -5) == -10
        assert add(-10, 20) == 10

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 10) == 0
        assert subtract(100, 50) == 50

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 0) == 0
        assert multiply(10, 10) == 100

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-5, -5) == 25
        assert multiply(-1, 100) == -100

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(100, 4) == 25

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5
        assert divide(-20, -4) == 5
        assert divide(10, -2) == -5

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_floats(self):
        """Test division with floating point numbers."""
        assert divide(7, 2) == 3.5
        assert divide(1, 3) == pytest.approx(0.333, rel=1e-2)


class TestAddition:
    """Test cases for the add function."""
    
    def test_add_positive_numbers_extended(self):
        """Test addition of two positive numbers."""
        assert add(5, 3) == 8
        assert add(10, 20) == 30
        assert add(99, 1) == 100
    
    def test_add_negative_numbers_extended(self):
        """Test addition of two negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -20) == -30
    
    def test_add_positive_and_negative(self):
        """Test addition of positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_zero(self):
        """Test addition with zero."""
        assert add(5, 0) == 5
        assert add(0, 0) == 0
        assert add(0, -5) == -5
    
    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestSubtraction:
    """Test cases for the subtract function."""
    
    def test_subtract_positive_numbers_extended(self):
        """Test subtraction of two positive numbers."""
        assert subtract(10, 3) == 7
        assert subtract(100, 50) == 50
    
    def test_subtract_negative_numbers_extended(self):
        """Test subtraction of two negative numbers."""
        assert subtract(-10, -3) == -7
        assert subtract(-5, -5) == 0
    
    def test_subtract_positive_and_negative(self):
        """Test subtraction of positive and negative numbers."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0
    
    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(3.3, 1.1) == pytest.approx(2.2)


class TestMultiplication:
    """Test cases for the multiply function."""
    
    def test_multiply_positive_numbers_extended(self):
        """Test multiplication of two positive numbers."""
        assert multiply(5, 3) == 15
        assert multiply(10, 10) == 100
    
    def test_multiply_negative_numbers_extended(self):
        """Test multiplication of two negative numbers."""
        assert multiply(-5, -3) == 15
        assert multiply(-4, -4) == 16
    
    def test_multiply_positive_and_negative(self):
        """Test multiplication of positive and negative numbers."""
        assert multiply(5, -3) == -15
        assert multiply(-5, 3) == -15
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_by_one(self):
        """Test multiplication by one."""
        assert multiply(5, 1) == 5
        assert multiply(-5, 1) == -5
    
    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 4) == 10.0
        assert multiply(1.5, 2.5) == pytest.approx(3.75)


class TestDivision:
    """Test cases for the divide function."""
    
    def test_divide_positive_numbers_extended(self):
        """Test division of two positive numbers."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
        assert divide(100, 10) == 10
    
    def test_divide_negative_numbers_extended(self):
        """Test division of two negative numbers."""
        assert divide(-10, -2) == 5
        assert divide(-20, -4) == 5
    
    def test_divide_positive_and_negative(self):
        """Test division of positive and negative numbers."""
        assert divide(10, -2) == -5
        assert divide(-10, 2) == -5
    
    def test_divide_floats_extended(self):
        """Test division with floating point numbers."""
        assert divide(10.0, 2.5) == pytest.approx(4.0)
        assert divide(7.5, 2.5) == 3.0
        assert divide(5, 2) == pytest.approx(2.5)
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0
    
    def test_divide_by_one(self):
        """Test division by one."""
        assert divide(5, 1) == 5
        assert divide(-5, 1) == -5


class TestEdgeCases:
    """Test cases for edge cases and special scenarios."""
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert multiply(10000, 100) == 1000000
        assert divide(1000000, 10) == 100000
    
    def test_very_small_floats(self):
        """Test operations with very small floating point numbers."""
        assert add(0.0001, 0.0002) == pytest.approx(0.0003)
    
    def test_mixed_int_and_float(self):
        """Test operations with mixed integer and float operands."""
        assert add(5, 2.5) == 7.5
        assert multiply(4, 2.5) == 10.0
        assert divide(10, 4) == 2.5
'''
    with open(test_file, 'w') as f:
        f.write(test_content)
