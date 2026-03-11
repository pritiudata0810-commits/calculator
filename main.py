"""
Command-line calculator application.
Performs basic arithmetic operations: addition, subtraction, multiplication, division.
"""

from calculator import add, subtract, multiply, divide


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("Simple Calculator")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 40)


def get_numbers():
    """Prompt user for two numbers and return them."""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers")
        return None, None


def main():
    """Main calculator loop."""
    while True:
        display_menu()
        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Error: Invalid choice. Please select 1-5")
            continue

        num1, num2 = get_numbers()
        if num1 is None:
            continue

        try:
            if choice == "1":
                result = add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"\nResult: {num1} × {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"\nResult: {num1} ÷ {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
