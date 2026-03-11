#!/usr/bin/env python
"""Script to create tests directory and files."""

import os
import pathlib

# Base directory
base_path = pathlib.Path('D:\\calculator\\calculator')

# Create tests directory
tests_dir = base_path / 'tests'
tests_dir.mkdir(parents=True, exist_ok=True)
print(f'Created directory: {tests_dir}')

# Create __init__.py (empty)
init_file = tests_dir / '__init__.py'
init_file.touch()
print(f'Created empty file: {init_file}')

# Test content
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
'''

# Create test_calculator.py
test_file = tests_dir / 'test_calculator.py'
test_file.write_text(test_content)
print(f'Created file: {test_file}')

# Verify files
print('\\nVerification:')
print(f'tests directory exists: {tests_dir.exists()}')
print(f'__init__.py exists: {init_file.exists()}')
print(f'test_calculator.py exists: {test_file.exists()}')
print(f'test_calculator.py size: {test_file.stat().st_size} bytes')

# List files in tests directory
print('\\nFiles in tests directory:')
for file in sorted(tests_dir.iterdir()):
    print(f'  - {file.name}')
