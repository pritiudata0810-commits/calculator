"""
Improved calculator module that provides basic arithmetic operations
and command-line expression evaluation.
"""

import sys
import re


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers.
    
    Raises:
        ValueError: If attempting to divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a number to a power."""
    return a ** b


def modulus(a, b):
    """Return the remainder of division."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b


def validate_expression(expression):
    """
    Validate that the expression contains only allowed characters.
    
    Args:
        expression: Mathematical expression string
        
    Returns:
        True if valid, raises ValueError otherwise
    """
    allowed_pattern = r'^[\d\s\+\-\*/%()\.]+$'
    if not re.match(allowed_pattern, expression):
        raise ValueError(
            f"Invalid characters in expression. Only numbers, operators (+, -, *, /, %, **), "
            f"parentheses, and spaces are allowed."
        )
    return True


def evaluate_expression(expression):
    """
    Safely evaluate a mathematical expression.
    
    Args:
        expression: Mathematical expression string (e.g., "5+3*2**4")
        
    Returns:
        The result of the expression evaluation
        
    Raises:
        ValueError: If expression is invalid or division by zero occurs
        SyntaxError: If expression has syntax errors
    """
    if not expression or not expression.strip():
        raise ValueError("Expression cannot be empty")
    
    validate_expression(expression)
    
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    except SyntaxError as e:
        raise SyntaxError(f"Invalid expression syntax: {e}")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")


def display_usage():
    """Display help message with usage examples."""
    usage_message = """
╔═══════════════════════════════════════════════════════════╗
║           COMMAND LINE CALCULATOR - USAGE GUIDE           ║
╚═══════════════════════════════════════════════════════════╝

Usage: python calculator.py "<expression>"

Description:
  Evaluates a mathematical expression and displays the result.

Supported Operators:
  +   Addition          Example: 5 + 3
  -   Subtraction       Example: 10 - 4
  *   Multiplication    Example: 7 * 6
  /   Division          Example: 20 / 4
  %   Modulus           Example: 17 % 5
  **  Power/Exponent    Example: 2 ** 8

Features:
  • Supports parentheses for order of operations: (5 + 3) * 2
  • Respects mathematical operator precedence
  • Handles floating-point numbers: 3.14 * 2

Examples:
  python calculator.py "5 + 3"           → Result: 8
  python calculator.py "5 + 3 * 2"       → Result: 11
  python calculator.py "5 + 3 * 2 ** 4"  → Result: 53
  python calculator.py "(5 + 3) * 2"     → Result: 16
  python calculator.py "10 / 2"          → Result: 5.0
  python calculator.py "17 % 5"          → Result: 2

Error Handling:
  • Missing arguments → Shows this usage message
  • Invalid characters → Error message with allowed operators
  • Division by zero → Error message
  • Invalid syntax → Error message with details

╚═══════════════════════════════════════════════════════════╝
    """
    print(usage_message)


def main():
    """Main function to handle command-line calculator execution."""
    if len(sys.argv) < 2:
        display_usage()
        sys.exit(0)
    
    expression = sys.argv[1]
    
    try:
        result = evaluate_expression(expression)
        
        print("\n" + "=" * 60)
        print(f"Expression: {expression}")
        print("=" * 60)
        print(f"Result:     {result}")
        print("=" * 60 + "\n")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}\n", file=sys.stderr)
        sys.exit(1)
    except SyntaxError as e:
        print(f"\n❌ Syntax Error: {e}\n", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}\n", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
