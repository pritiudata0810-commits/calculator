#!/usr/bin/env python3
"""
Direct setup script - creates test directory and files without subprocess calls.
"""

import os
import sys

# Ensure we're in the right directory
os.chdir(r'D:\calculator\calculator')

def setup_tests():
    """Create test directory structure."""
    
    tests_dir = 'tests'
    
    # Create tests directory
    os.makedirs(tests_dir, exist_ok=True)
    print(f"✓ Created directory: {os.path.abspath(tests_dir)}")
    
    # Create __init__.py (empty)
    init_file = os.path.join(tests_dir, '__init__.py')
    with open(init_file, 'w') as f:
        f.write('')
    print(f"✓ Created file: __init__.py")
    
    # Create test_calculator.py with exact content
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
    
    with open(test_file, 'w') as f:
        f.write(test_content)
    print(f"✓ Created file: test_calculator.py")
    
    # Verification with os module
    print("\n" + "="*70)
    print("VERIFICATION - Directory Contents with File Sizes")
    print("="*70 + "\n")
    
    abs_tests_dir = os.path.abspath(tests_dir)
    print(f"Directory Path: {abs_tests_dir}\n")
    
    # Display files with sizes
    print(f"{'Filename':<30} {'Size (bytes)':<15} {'Path'}")
    print("-" * 80)
    
    for filename in sorted(os.listdir(tests_dir)):
        filepath = os.path.join(tests_dir, filename)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            abs_path = os.path.abspath(filepath)
            print(f"{filename:<30} {size:<15d} {abs_path}")
    
    # Summary statistics
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    total_size = 0
    file_count = 0
    for filename in os.listdir(tests_dir):
        filepath = os.path.join(tests_dir, filename)
        if os.path.isfile(filepath):
            total_size += os.path.getsize(filepath)
            file_count += 1
    
    print(f"Total files created: {file_count}")
    print(f"Total size: {total_size} bytes")
    print(f"Directory exists: {os.path.isdir(tests_dir)}")
    print(f"Directory is readable: {os.access(tests_dir, os.R_OK)}")
    print(f"Directory is writable: {os.access(tests_dir, os.W_OK)}")
    print("\n✓ Test directory structure created successfully!")

if __name__ == '__main__':
    try:
        setup_tests()
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
