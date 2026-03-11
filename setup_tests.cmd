@echo off
REM Create tests directory
mkdir "D:\calculator\calculator\tests" 2>nul

REM Create __init__.py (empty file)
type nul > "D:\calculator\calculator\tests\__init__.py"

REM Create test_calculator.py with content
(
echo """
echo Unit tests for the calculator module.
echo """
echo.
echo import pytest
echo from calculator import add, subtract, multiply, divide
echo.
echo.
echo class TestBasicOperations:
echo     """Test basic arithmetic operations."""
echo.
echo     def test_add_positive_numbers^(self^):
echo         """Test addition of positive numbers."""
echo         assert add^(2, 3^) == 5
echo         assert add^(0, 5^) == 5
echo         assert add^(100, 50^) == 150
echo.
echo     def test_add_negative_numbers^(self^):
echo         """Test addition with negative numbers."""
echo         assert add^(-2, 3^) == 1
echo         assert add^(-5, -5^) == -10
echo         assert add^(-10, 20^) == 10
echo.
echo     def test_subtract_positive_numbers^(self^):
echo         """Test subtraction of positive numbers."""
echo         assert subtract^(5, 3^) == 2
echo         assert subtract^(10, 10^) == 0
echo         assert subtract^(100, 50^) == 50
echo.
echo     def test_subtract_negative_numbers^(self^):
echo         """Test subtraction with negative numbers."""
echo         assert subtract^(-5, -3^) == -2
echo         assert subtract^(5, -3^) == 8
echo         assert subtract^(-5, 3^) == -8
echo.
echo     def test_multiply_positive_numbers^(self^):
echo         """Test multiplication of positive numbers."""
echo         assert multiply^(2, 3^) == 6
echo         assert multiply^(5, 0^) == 0
echo         assert multiply^(10, 10^) == 100
echo.
echo     def test_multiply_negative_numbers^(self^):
echo         """Test multiplication with negative numbers."""
echo         assert multiply^(-2, 3^) == -6
echo         assert multiply^(-5, -5^) == 25
echo         assert multiply^(-1, 100^) == -100
echo.
echo     def test_divide_positive_numbers^(self^):
echo         """Test division of positive numbers."""
echo         assert divide^(10, 2^) == 5
echo         assert divide^(9, 3^) == 3
echo         assert divide^(100, 4^) == 25
echo.
echo     def test_divide_negative_numbers^(self^):
echo         """Test division with negative numbers."""
echo         assert divide^(-10, 2^) == -5
echo         assert divide^(-20, -4^) == 5
echo         assert divide^(10, -2^) == -5
echo.
echo     def test_divide_by_zero^(self^):
echo         """Test that dividing by zero raises ValueError."""
echo         with pytest.raises^(ValueError, match="Cannot divide by zero"^):
echo             divide^(10, 0^)
echo.
echo     def test_divide_floats^(self^):
echo         """Test division with floating point numbers."""
echo         assert divide^(7, 2^) == 3.5
echo         assert divide^(1, 3^) == pytest.approx^(0.333, rel=1e-2^)
) > "D:\calculator\calculator\tests\test_calculator.py"

REM Verify the files were created
echo.
echo ======================================================================
echo Verification - Files Created:
echo ======================================================================
if exist "D:\calculator\calculator\tests\__init__.py" (
    echo. ✓ __init__.py created successfully
    for %%A in ("D:\calculator\calculator\tests\__init__.py") do echo   Size: %%~zA bytes
)
if exist "D:\calculator\calculator\tests\test_calculator.py" (
    echo. ✓ test_calculator.py created successfully
    for %%A in ("D:\calculator\calculator\tests\test_calculator.py") do echo   Size: %%~zA bytes
)

echo.
echo ======================================================================
echo Directory Listing:
echo ======================================================================
dir "D:\calculator\calculator\tests"

echo.
echo ✓ Task completed!
