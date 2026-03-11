@echo off
python.exe -c "
import os
tests_dir = r'D:\calculator\calculator\tests'
os.makedirs(tests_dir, exist_ok=True)
with open(os.path.join(tests_dir, '__init__.py'), 'w') as f:
    f.write('')
with open(os.path.join(tests_dir, 'test_calculator.py'), 'w') as f:
    f.write('''\"\"\"Unit tests for the calculator module.\"\"\"
import pytest
from calculator import add, subtract, multiply, divide

class TestBasicOperations:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(0, 5) == 5
        assert add(100, 50) == 150
    def test_add_negative_numbers(self):
        assert add(-2, 3) == 1
        assert add(-5, -5) == -10
        assert add(-10, 20) == 10
    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2
        assert subtract(10, 10) == 0
        assert subtract(100, 50) == 50
    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6
        assert multiply(5, 0) == 0
        assert multiply(10, 10) == 100
    def test_multiply_negative_numbers(self):
        assert multiply(-2, 3) == -6
        assert multiply(-5, -5) == 25
        assert multiply(-1, 100) == -100
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(100, 4) == 25
    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5
        assert divide(-20, -4) == 5
        assert divide(10, -2) == -5
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match=\"Cannot divide by zero\"):
            divide(10, 0)
    def test_divide_floats(self):
        assert divide(7, 2) == 3.5
        assert divide(1, 3) == pytest.approx(0.333, rel=1e-2)
''')
print('All files created successfully!')
"
pause
