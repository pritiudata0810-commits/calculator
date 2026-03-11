#!/usr/bin/env python3
"""
Create the tests directory and test files for the calculator project.
This script uses only standard library functions that should work in any Python environment.
"""

import os
import sys
from pathlib import Path

def main():
    # Create the tests directory
    tests_dir = Path(r'D:\calculator\calculator\tests')
    tests_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Tests directory created: {tests_dir}")
    
    # Create __init__.py
    init_file = tests_dir / '__init__.py'
    init_file.write_text('')
    print(f"✓ Created: {init_file}")
    
    # Create test_calculator.py
    test_file = tests_dir / 'test_calculator.py'
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
    test_file.write_text(test_content)
    print(f"✓ Created: {test_file}")
    
    # Verify and display results
    print("\n" + "="*60)
    print("VERIFICATION")
    print("="*60)
    
    print("\nDirectory listing:")
    for item in sorted(tests_dir.iterdir()):
        size = item.stat().st_size if item.is_file() else 0
        item_type = "FILE" if item.is_file() else "DIR"
        print(f"  {item.name:30s} ({item_type:3s}) {size:6d} bytes")
    
    print("\nFile sizes summary:")
    total_size = 0
    for file_path in [init_file, test_file]:
        size = file_path.stat().st_size
        total_size += size
        print(f"  {file_path.name:30s} {size:6d} bytes")
    print(f"  {'TOTAL':30s} {total_size:6d} bytes")
    
    print("\n✓ All files created successfully!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
