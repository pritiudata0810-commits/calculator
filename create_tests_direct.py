#!/usr/bin/env python3
"""
Direct file creation and verification script.
"""
import os
import sys

def create_test_files():
    """Create test directory and test files."""
    tests_dir = r'D:\calculator\calculator\tests'
    
    # Create directory
    os.makedirs(tests_dir, exist_ok=True)
    print(f"✓ Created/verified directory: {tests_dir}")
    
    # Create __init__.py
    init_file = os.path.join(tests_dir, '__init__.py')
    with open(init_file, 'w') as f:
        pass
    print(f"✓ Created file: {init_file}")
    
    # Create test_calculator.py
    test_file = os.path.join(tests_dir, 'test_calculator.py')
    content = '''"""
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
        f.write(content)
    print(f"✓ Created file: {test_file}")
    
    # Verification
    print("\n" + "=" * 70)
    print("VERIFICATION - Directory Contents")
    print("=" * 70)
    
    if os.path.exists(tests_dir):
        files = sorted(os.listdir(tests_dir))
        for file in files:
            file_path = os.path.join(tests_dir, file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                print(f"  {file:<30} {size:>8} bytes")
        
        print("=" * 70)
        print(f"\nSummary:")
        print(f"  Total files created: {len(files)}")
        print(f"  Directory location: {tests_dir}")
        print(f"  All files exist: {all(os.path.exists(os.path.join(tests_dir, f)) for f in files)}")
        print("\n✓ Test file setup completed successfully!")
        return True
    else:
        print("ERROR: Directory was not created!")
        return False

if __name__ == '__main__':
    success = create_test_files()
    sys.exit(0 if success else 1)
