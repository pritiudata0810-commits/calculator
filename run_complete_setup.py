#!/usr/bin/env python3
"""
Complete execution of test setup with full output and verification.
"""
import os
import sys

print("=" * 70)
print("EXECUTING: create_tests_dir.py")
print("=" * 70)
print()

# Create the tests directory
tests_dir = 'D:/calculator/calculator/tests'
os.makedirs(tests_dir, exist_ok=True)
print(f"✓ Tests directory created successfully: {tests_dir}")

# Create __init__.py
init_file = os.path.join(tests_dir, '__init__.py')
with open(init_file, 'w') as f:
    f.write('')
print(f"✓ Created: {init_file}")

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
with open(test_file, 'w') as f:
    f.write(test_content)
print(f"✓ Created: {test_file}")

print("\n✓ All files created successfully!")

print()
print("=" * 70)
print("VERIFICATION: Directory and File Status")
print("=" * 70)
print()

# Verify the directory
tests_dir_path = 'D:\\calculator\\calculator\\tests'
if os.path.exists(tests_dir_path) and os.path.isdir(tests_dir_path):
    print(f"✓ Directory exists: {tests_dir_path}")
    print(f"  Directory path (absolute): {os.path.abspath(tests_dir_path)}")
else:
    print(f"✗ Directory NOT found: {tests_dir_path}")
    sys.exit(1)

# List directory contents
print(f"\n✓ Directory contents:")
contents = os.listdir(tests_dir_path)
for item in sorted(contents):
    item_path = os.path.join(tests_dir_path, item)
    if os.path.isfile(item_path):
        size = os.path.getsize(item_path)
        print(f"  - {item} ({size} bytes)")
    else:
        print(f"  - {item}/ (directory)")

# Verify specific files exist and show their properties
print(f"\n✓ File verification:")
init_path = os.path.join(tests_dir_path, '__init__.py')
test_path = os.path.join(tests_dir_path, 'test_calculator.py')

if os.path.exists(init_path):
    size = os.path.getsize(init_path)
    print(f"  ✓ __init__.py exists ({size} bytes)")
else:
    print(f"  ✗ __init__.py NOT found")

if os.path.exists(test_path):
    size = os.path.getsize(test_path)
    print(f"  ✓ test_calculator.py exists ({size} bytes)")
    with open(test_path, 'r') as f:
        line_count = len(f.readlines())
    print(f"    Total lines: {line_count}")
    
    # Show first few lines
    print(f"\n  First 10 lines of test_calculator.py:")
    with open(test_path, 'r') as f:
        for i, line in enumerate(f):
            if i < 10:
                print(f"    {i+1:3}: {line.rstrip()}")
            else:
                break
else:
    print(f"  ✗ test_calculator.py NOT found")

print()
print("=" * 70)
print("✓ SETUP COMPLETE - All tests directory and files created successfully!")
print("=" * 70)
