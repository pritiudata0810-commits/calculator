"""
MASTER SETUP FILE - Creates test directory and files
This file performs the exact operations requested.

USAGE:
------
Option 1 (Recommended): python master_setup.py
Option 2: python -m master_setup
Option 3: Double-click master_setup.pyw (Windows)

This script will:
1. Create D:\calculator\calculator\tests directory
2. Create tests/__init__.py (empty file)
3. Create tests/test_calculator.py with complete test suite
4. Display verification report with file sizes
"""

import os
import sys
from pathlib import Path

def create_test_files():
    """Create the test directory structure and files."""
    
    # Define paths
    base_dir = Path(__file__).parent
    tests_dir = base_dir / 'tests'
    init_file = tests_dir / '__init__.py'
    test_file = tests_dir / 'test_calculator.py'
    
    print("\n" + "=" * 80)
    print("TEST FILE CREATION UTILITY")
    print("=" * 80)
    
    # Step 1: Create directory
    print(f"\n[1/3] Creating directory: {tests_dir}")
    try:
        tests_dir.mkdir(exist_ok=True)
        print(f"      ✓ Directory created/verified")
    except Exception as e:
        print(f"      ✗ Error: {e}")
        return False
    
    # Step 2: Create __init__.py
    print(f"\n[2/3] Creating __init__.py")
    try:
        init_file.write_text('')
        print(f"      ✓ File created: {init_file}")
    except Exception as e:
        print(f"      ✗ Error: {e}")
        return False
    
    # Step 3: Create test_calculator.py
    print(f"\n[3/3] Creating test_calculator.py")
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
        test_file.write_text(test_content)
        print(f"      ✓ File created: {test_file}")
    except Exception as e:
        print(f"      ✗ Error: {e}")
        return False
    
    # Verification
    print("\n" + "=" * 80)
    print("VERIFICATION REPORT")
    print("=" * 80)
    
    print(f"\nDirectory: {tests_dir}")
    print(f"Exists: {tests_dir.exists()}")
    
    if tests_dir.exists():
        files = sorted(list(tests_dir.glob('*')))
        
        print(f"\n{'Filename':<35} {'Size (bytes)':<20} {'Status':<10}")
        print("-" * 65)
        
        for file_path in files:
            if file_path.is_file():
                size = file_path.stat().st_size
                status = "✓" if size >= 0 else "✗"
                print(f"{file_path.name:<35} {size:<20} {status:<10}")
        
        print("-" * 65)
        print(f"\nTotal files created: {len(files)}")
        
        expected_files = {'__init__.py', 'test_calculator.py'}
        actual_files = {f.name for f in files if f.is_file()}
        all_present = expected_files.issubset(actual_files)
        
        print(f"All expected files present: {'✓ Yes' if all_present else '✗ No'}")
        
        if all_present:
            print("\n" + "=" * 80)
            print("✓ SETUP COMPLETED SUCCESSFULLY!")
            print("=" * 80)
            print("\nYour test files are ready:")
            print(f"  • Directory: {tests_dir}")
            print(f"  • Tests module: {test_file.name}")
            print(f"  • Init file: __init__.py")
            print("\nYou can now run: pytest")
            return True
        else:
            print("\n✗ Some expected files are missing!")
            return False
    else:
        print("\n✗ Tests directory was not created!")
        return False

def main():
    """Main entry point."""
    try:
        success = create_test_files()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
