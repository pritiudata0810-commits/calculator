import os
import sys

# Change to the calculator directory
os.chdir(r'D:\calculator\calculator')

# Create the tests directory
tests_dir = 'tests'
os.makedirs(tests_dir, exist_ok=True)

# Create __init__.py (empty)
with open(os.path.join(tests_dir, '__init__.py'), 'w') as f:
    f.write('')

# Create test_calculator.py with the exact content
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

with open(os.path.join(tests_dir, 'test_calculator.py'), 'w') as f:
    f.write(test_content)

# Verify files were created and display with sizes
print("=" * 70)
print("FILE CREATION AND VERIFICATION REPORT")
print("=" * 70)

print("\nDirectory Structure:")
for root, dirs, files in os.walk('tests'):
    level = root.replace('tests', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in sorted(files):
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)
        print(f'{subindent}{file:<30} {size:>10} bytes')

print("\n" + "=" * 70)
print("Individual File Details:")
print("=" * 70)

for file_name in sorted(os.listdir(tests_dir)):
    file_path = os.path.join(tests_dir, file_name)
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        print(f"\n  File: {file_name}")
        print(f"  Size: {size} bytes")
        print(f"  Full path: {os.path.abspath(file_path)}")
        print(f"  Exists: {os.path.exists(file_path)}")

print("\n" + "=" * 70)
print("✓ Files created and verified successfully!")
print("=" * 70)
