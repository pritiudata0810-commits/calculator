"""
Professional Calculator with Advanced Features
A feature-rich command-line calculator with calculation history, advanced math operations,
and comprehensive error handling.
"""

import math
import sys
from datetime import datetime


class ProfessionalCalculator:
    """A professional calculator with history tracking and advanced operations."""

    def __init__(self):
        """Initialize the calculator with empty history."""
        self.history = []
        self.running = True

    def display_banner(self):
        """Display an attractive ASCII art banner."""
        banner = """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║        ████████╗██████╗ ██████╗     ██████╗ █████╗        ║
║        ╚══██╔══╝██╔══██╗██╔═══██╗   ██╔════╝██╔══██╗       ║
║           ██║   ██████╔╝██║   ██║   ██║     ███████║       ║
║           ██║   ██╔═══╝ ██║   ██║   ██║     ██╔══██║       ║
║           ██║   ██║     ╚██████╔╝   ╚██████╗██║  ██║       ║
║           ╚═╝   ╚═╝      ╚═════╝     ╚═════╝╚═╝  ╚═╝       ║
║                                                            ║
║          Professional Calculator v1.0                     ║
║          Advanced Math Operations & History               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def display_menu(self):
        """Display the main operation menu."""
        menu = """
┌─────────────────────────────────────────────────────────────┐
│                    AVAILABLE OPERATIONS                     │
├─────────────────────────────────────────────────────────────┤
│  Basic Operations:                                          │
│    [1]  Addition          (+)   │  [2]  Subtraction    (-)  │
│    [3]  Multiplication    (*)   │  [4]  Division       (/)  │
│                                                             │
│  Advanced Operations:                                       │
│    [5]  Power             (x^y) │  [6]  Square Root    (√)  │
│    [7]  Modulo            (%)   │  [8]  Absolute Value (|x|)│
│    [9]  Percentage              │  [10] Factorial      (n!) │
│                                                             │
│  History & Settings:                                        │
│    [11] View History            │  [12] Clear History       │
│    [13] Exit Calculator                                    │
└─────────────────────────────────────────────────────────────┘
        """
        print(menu)

    def get_safe_float(self, prompt):
        """
        Safely get a float input from the user with error handling.
        
        Args:
            prompt (str): The prompt to display to the user.
            
        Returns:
            float: The validated float input, or None if invalid.
        """
        try:
            value = input(prompt)
            if not value.strip():
                print("❌ Error: Input cannot be empty. Please try again.")
                return None
            result = float(value)
            return result
        except ValueError:
            print(f"❌ Error: '{value}' is not a valid number. Please enter a numeric value.")
            return None

    def get_safe_int(self, prompt):
        """
        Safely get an integer input from the user with error handling.
        
        Args:
            prompt (str): The prompt to display to the user.
            
        Returns:
            int: The validated integer input, or None if invalid.
        """
        try:
            value = input(prompt)
            if not value.strip():
                print("❌ Error: Input cannot be empty. Please try again.")
                return None
            result = int(value)
            return result
        except ValueError:
            print(f"❌ Error: '{value}' is not a valid integer. Please enter a whole number.")
            return None

    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.record_operation(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        """Subtract two numbers."""
        result = a - b
        self.record_operation(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.record_operation(f"{a} × {b}", result)
        return result

    def divide(self, a, b):
        """
        Divide two numbers with zero-division checking.
        
        Raises:
            ValueError: If attempting to divide by zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.record_operation(f"{a} ÷ {b}", result)
        return result

    def power(self, base, exponent):
        """
        Calculate base raised to the power of exponent.
        
        Raises:
            ValueError: If operation results in overflow.
        """
        try:
            result = base ** exponent
            self.record_operation(f"{base}^{exponent}", result)
            return result
        except OverflowError:
            raise ValueError("Result is too large to calculate")

    def square_root(self, number):
        """
        Calculate the square root of a number.
        
        Raises:
            ValueError: If attempting to calculate root of negative number.
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        result = math.sqrt(number)
        self.record_operation(f"√{number}", result)
        return result

    def modulo(self, a, b):
        """
        Calculate the modulo (remainder) of two numbers.
        
        Raises:
            ValueError: If divisor is zero.
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero divisor")
        result = a % b
        self.record_operation(f"{a} % {b}", result)
        return result

    def absolute_value(self, number):
        """Calculate the absolute value of a number."""
        result = abs(number)
        self.record_operation(f"|{number}|", result)
        return result

    def percentage(self, value, percent):
        """
        Calculate the percentage of a value.
        
        Args:
            value (float): The base value.
            percent (float): The percentage to calculate.
            
        Returns:
            float: The calculated percentage.
        """
        result = (value * percent) / 100
        self.record_operation(f"{percent}% of {value}", result)
        return result

    def factorial(self, number):
        """
        Calculate the factorial of a number.
        
        Raises:
            ValueError: If number is negative or not an integer.
        """
        if number < 0:
            raise ValueError("Factorial cannot be calculated for negative numbers")
        if not isinstance(number, int) or number != int(number):
            raise ValueError("Factorial requires a whole number")
        
        result = math.factorial(int(number))
        self.record_operation(f"{int(number)}!", result)
        return result

    def record_operation(self, operation, result):
        """
        Record a calculation in the history.
        
        Args:
            operation (str): Description of the operation.
            result (float): The result of the calculation.
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "operation": operation,
            "result": result
        }
        self.history.append(entry)

    def view_history(self):
        """Display the calculation history."""
        if not self.history:
            print("\n📭 History is empty. No calculations yet.")
            return
        
        print("\n" + "="*60)
        print("📋 CALCULATION HISTORY")
        print("="*60)
        
        for idx, entry in enumerate(self.history, 1):
            timestamp = entry["timestamp"]
            operation = entry["operation"]
            result = entry["result"]
            
            # Format result for cleaner display
            if isinstance(result, float) and result == int(result):
                result_str = str(int(result))
            else:
                result_str = f"{result:.10g}"  # Remove trailing zeros
            
            print(f"{idx:2d}. [{timestamp}] {operation:20s} = {result_str}")
        
        print("="*60 + "\n")

    def clear_history(self):
        """Clear the calculation history with confirmation."""
        if not self.history:
            print("\n📭 History is already empty.")
            return
        
        confirmation = input("\n⚠️  Are you sure you want to clear all history? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            self.history.clear()
            print("✅ History cleared successfully.\n")
        else:
            print("❌ History clear cancelled.\n")

    def handle_operation(self, choice):
        """
        Handle the selected operation.
        
        Args:
            choice (str): The user's menu choice.
            
        Returns:
            bool: True if operation succeeded, False otherwise.
        """
        try:
            if choice == '1':
                a = self.get_safe_float("Enter first number: ")
                if a is None:
                    return False
                b = self.get_safe_float("Enter second number: ")
                if b is None:
                    return False
                result = self.add(a, b)
                print(f"\n✅ Result: {a} + {b} = {result}\n")

            elif choice == '2':
                a = self.get_safe_float("Enter first number: ")
                if a is None:
                    return False
                b = self.get_safe_float("Enter second number: ")
                if b is None:
                    return False
                result = self.subtract(a, b)
                print(f"\n✅ Result: {a} - {b} = {result}\n")

            elif choice == '3':
                a = self.get_safe_float("Enter first number: ")
                if a is None:
                    return False
                b = self.get_safe_float("Enter second number: ")
                if b is None:
                    return False
                result = self.multiply(a, b)
                print(f"\n✅ Result: {a} × {b} = {result}\n")

            elif choice == '4':
                a = self.get_safe_float("Enter numerator: ")
                if a is None:
                    return False
                b = self.get_safe_float("Enter denominator: ")
                if b is None:
                    return False
                result = self.divide(a, b)
                print(f"\n✅ Result: {a} ÷ {b} = {result}\n")

            elif choice == '5':
                base = self.get_safe_float("Enter base number: ")
                if base is None:
                    return False
                exponent = self.get_safe_float("Enter exponent: ")
                if exponent is None:
                    return False
                result = self.power(base, exponent)
                print(f"\n✅ Result: {base}^{exponent} = {result}\n")

            elif choice == '6':
                number = self.get_safe_float("Enter a number to find square root: ")
                if number is None:
                    return False
                result = self.square_root(number)
                print(f"\n✅ Result: √{number} = {result}\n")

            elif choice == '7':
                a = self.get_safe_float("Enter dividend: ")
                if a is None:
                    return False
                b = self.get_safe_float("Enter divisor: ")
                if b is None:
                    return False
                result = self.modulo(a, b)
                print(f"\n✅ Result: {a} % {b} = {result}\n")

            elif choice == '8':
                number = self.get_safe_float("Enter a number: ")
                if number is None:
                    return False
                result = self.absolute_value(number)
                print(f"\n✅ Result: |{number}| = {result}\n")

            elif choice == '9':
                value = self.get_safe_float("Enter base value: ")
                if value is None:
                    return False
                percent = self.get_safe_float("Enter percentage: ")
                if percent is None:
                    return False
                result = self.percentage(value, percent)
                print(f"\n✅ Result: {percent}% of {value} = {result}\n")

            elif choice == '10':
                number = self.get_safe_int("Enter a whole number for factorial: ")
                if number is None:
                    return False
                result = self.factorial(number)
                print(f"\n✅ Result: {number}! = {result}\n")

            elif choice == '11':
                self.view_history()

            elif choice == '12':
                self.clear_history()

            elif choice == '13':
                print("\n👋 Thank you for using the Professional Calculator!")
                print("📊 Total calculations performed:", len(self.history))
                self.running = False

            else:
                print("❌ Invalid choice. Please select an option from 1 to 13.\n")
                return False

            return True

        except ValueError as e:
            print(f"❌ Error: {e}\n")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")
            return False

    def run(self):
        """Main loop to run the calculator."""
        self.display_banner()
        
        while self.running:
            self.display_menu()
            choice = input("Enter your choice (1-13): ").strip()
            self.handle_operation(choice)
        
        # Display final summary
        if self.history:
            print("\n" + "="*60)
            print("📊 FINAL CALCULATION SUMMARY")
            print("="*60)
            print(f"Total calculations: {len(self.history)}")
            print(f"Session time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*60)


def main():
    """Entry point for the calculator application."""
    calculator = ProfessionalCalculator()
    try:
        calculator.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Calculator interrupted by user. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
