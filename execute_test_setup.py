#!/usr/bin/env python3
"""
Direct test directory creation script.
This script creates the tests directory structure with comprehensive test cases.
"""
import os
import sys

def main():
    """Create tests directory and files."""
    tests_dir = r'D:\calculator\calculator\tests'
    
    # Create the tests directory
    try:
        os.makedirs(tests_dir, exist_ok=True)
        print(f"✓ Tests directory created successfully: {tests_dir}")
    except Exception as e:
        print(f"✗ Error creating tests directory: {e}")
        return False
    
    # Create __init__.py
    try:
        init_file = os.path.join(tests_dir, '__init__.py')
        with open(init_file, 'w') as f:
            f.write('')
        print(f"✓ Created: {init_file}")
    except Exception as e:
        print(f"✗ Error creating __init__.py: {e}")
        return False
    
    # Create test_calculator.py with comprehensive tests
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
    
    try:
        test_file = os.path.join(tests_dir, 'test_calculator.py')
        with open(test_file, 'w') as f:
            f.write(test_content)
        print(f"✓ Created: {test_file}")
    except Exception as e:
        print(f"✗ Error creating test_calculator.py: {e}")
        return False
    
    # Verify all files exist
    print("\n" + "="*50)
    print("VERIFICATION")
    print("="*50)
    
    all_good = True
    
    if os.path.isdir(tests_dir):
        print(f"✓ Tests directory exists")
    else:
        print(f"✗ Tests directory missing")
        all_good = False
    
    init_file = os.path.join(tests_dir, '__init__.py')
    if os.path.isfile(init_file):
        file_size = os.path.getsize(init_file)
        print(f"✓ __init__.py exists ({file_size} bytes)")
    else:
        print(f"✗ __init__.py missing")
        all_good = False
    
    test_file = os.path.join(tests_dir, 'test_calculator.py')
    if os.path.isfile(test_file):
        file_size = os.path.getsize(test_file)
        print(f"✓ test_calculator.py exists ({file_size} bytes)")
    else:
        print(f"✗ test_calculator.py missing")
        all_good = False
    
    # List directory contents
    print("\n" + "="*50)
    print("DIRECTORY CONTENTS: " + tests_dir)
    print("="*50)
    
    try:
        items = os.listdir(tests_dir)
        for item in sorted(items):
            item_path = os.path.join(tests_dir, item)
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
                print(f"  [FILE] {item:25} ({size:>6} bytes)")
            elif os.path.isdir(item_path):
                print(f"  [DIR]  {item}/")
    except Exception as e:
        print(f"✗ Error listing directory: {e}")
        all_good = False
    
    print("\n" + "="*50)
    if all_good:
        print("✓ ALL FILES CREATED SUCCESSFULLY!")
    else:
        print("✗ SOME FILES FAILED TO CREATE")
    print("="*50)
    
    return all_good

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
