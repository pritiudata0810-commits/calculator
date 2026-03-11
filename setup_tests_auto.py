"""
Auto-setup module that creates test structure on import.
"""
import os
import sys

# Setup tests directory when this module is imported
_tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
os.makedirs(_tests_dir, exist_ok=True)

# Create __init__.py if missing
_init_file = os.path.join(_tests_dir, '__init__.py')
if not os.path.exists(_init_file):
    open(_init_file, 'w').close()

# Create test_calculator.py with exact content
_test_file = os.path.join(_tests_dir, 'test_calculator.py')
if not os.path.exists(_test_file) or os.path.getsize(_test_file) < 100:
    _content = '''"""
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
    with open(_test_file, 'w') as f:
        f.write(_content)

# Print verification
if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("TEST FILE SETUP VERIFICATION")
    print("=" * 70)
    
    if os.path.exists(_tests_dir):
        files = sorted(os.listdir(_tests_dir))
        for file in files:
            file_path = os.path.join(_tests_dir, file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                print(f"  {file:<30} {size:>8} bytes")
        
        print("=" * 70)
        print(f"\nSummary:")
        print(f"  Directory: {_tests_dir}")
        print(f"  Total files: {len(files)}")
        print(f"  Files created: __init__.py, test_calculator.py")
        print("\n✓ Test files setup completed!")
    else:
        print(f"ERROR: Failed to create directory {_tests_dir}")
