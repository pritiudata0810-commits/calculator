#!/usr/bin/env python3
"""
Ultimate fallback test setup - creates test structure with minimal dependencies.
Run with: python setup_minimal.py
"""
import os
import sys

def create_test_structure():
    """Create the complete test directory structure."""
    
    # Determine the base directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(script_dir, 'tests')
    
    # Create tests directory
    try:
        os.makedirs(tests_dir, exist_ok=True)
        print(f"✓ Created directory: {tests_dir}")
    except OSError as e:
        print(f"✗ Failed to create tests directory: {e}")
        return False
    
    # Create __init__.py
    init_path = os.path.join(tests_dir, '__init__.py')
    try:
        with open(init_path, 'w') as f:
            f.write('')
        print(f"✓ Created file: __init__.py")
    except IOError as e:
        print(f"✗ Failed to create __init__.py: {e}")
        return False
    
    # Create test_calculator.py
    test_path = os.path.join(tests_dir, 'test_calculator.py')
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
        with open(test_path, 'w') as f:
            f.write(test_content)
        print(f"✓ Created file: test_calculator.py")
    except IOError as e:
        print(f"✗ Failed to create test_calculator.py: {e}")
        return False
    
    # Verify the structure
    print("\n" + "=" * 70)
    print("VERIFICATION - Directory Contents with File Sizes")
    print("=" * 70 + "\n")
    
    print(f"Directory Path: {tests_dir}\n")
    print(f"{'Filename':<30} {'Size (bytes)':<15} {'Path'}")
    print("-" * 80)
    
    total_size = 0
    file_count = 0
    
    try:
        for filename in sorted(os.listdir(tests_dir)):
            filepath = os.path.join(tests_dir, filename)
            if os.path.isfile(filepath):
                size = os.path.getsize(filepath)
                abs_path = os.path.abspath(filepath)
                print(f"{filename:<30} {size:<15d} {abs_path}")
                total_size += size
                file_count += 1
    except OSError as e:
        print(f"✗ Failed to verify directory: {e}")
        return False
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    print(f"Total files created: {file_count}")
    print(f"Total size: {total_size} bytes")
    print(f"Directory exists: {os.path.isdir(tests_dir)}")
    print(f"Directory is readable: {os.access(tests_dir, os.R_OK)}")
    print(f"Directory is writable: {os.access(tests_dir, os.W_OK)}")
    print("\n✓ Test directory structure created successfully!")
    
    return True

if __name__ == '__main__':
    success = create_test_structure()
    sys.exit(0 if success else 1)
