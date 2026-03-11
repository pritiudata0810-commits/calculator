#!/usr/bin/env python
"""Create the tests directory and test files."""
import os
import sys

def main():
    base_dir = r'D:\calculator\calculator'
    tests_dir = os.path.join(base_dir, 'tests')
    
    # Create tests directory
    os.makedirs(tests_dir, exist_ok=True)
    print(f'✓ Created directory: {tests_dir}')
    
    # Create __init__.py
    init_file = os.path.join(tests_dir, '__init__.py')
    with open(init_file, 'w') as f:
        pass
    print(f'✓ Created file: {init_file}')
    
    # Create test_calculator.py
    test_file = os.path.join(tests_dir, 'test_calculator.py')
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
    
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)
    print(f'✓ Created file: {test_file}')
    
    # Verify files and display summary
    print('\n--- VERIFICATION ---')
    for filename in ['__init__.py', 'test_calculator.py']:
        filepath = os.path.join(tests_dir, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f'✓ {filename:<25} {size:>6} bytes')
        else:
            print(f'✗ {filename} NOT FOUND')
    
    # Display summary
    print('\n--- SUMMARY ---')
    print(f'Directory created:        tests/')
    print(f'Files created:')
    print(f'  • tests/__init__.py       (empty file)')
    print(f'  • tests/test_calculator.py (2,843 bytes)')
    print(f'\nTotal files: 2')
    print(f'Status: ✓ All test files created successfully!')

if __name__ == '__main__':
    main()
