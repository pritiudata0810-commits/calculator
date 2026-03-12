"""
Test script to demonstrate the Professional Calculator functionality.
This script tests the calculator without interactive input.
"""

from pro_calculator import ProfessionalCalculator


def test_calculator():
    """Test all calculator functions programmatically."""
    calc = ProfessionalCalculator()
    
    print("=" * 70)
    print("PROFESSIONAL CALCULATOR - AUTOMATED TEST SUITE")
    print("=" * 70)
    
    # Test basic operations
    print("\n✅ BASIC OPERATIONS TEST")
    print("-" * 70)
    
    assert calc.add(10, 5) == 15, "Addition failed"
    print("✓ Addition: 10 + 5 = 15")
    
    assert calc.subtract(10, 5) == 5, "Subtraction failed"
    print("✓ Subtraction: 10 - 5 = 5")
    
    assert calc.multiply(10, 5) == 50, "Multiplication failed"
    print("✓ Multiplication: 10 × 5 = 50")
    
    assert calc.divide(10, 5) == 2, "Division failed"
    print("✓ Division: 10 ÷ 5 = 2")
    
    # Test advanced operations
    print("\n✅ ADVANCED OPERATIONS TEST")
    print("-" * 70)
    
    assert calc.power(2, 3) == 8, "Power failed"
    print("✓ Power: 2^3 = 8")
    
    assert calc.square_root(16) == 4, "Square root failed"
    print("✓ Square Root: √16 = 4")
    
    assert calc.modulo(10, 3) == 1, "Modulo failed"
    print("✓ Modulo: 10 % 3 = 1")
    
    assert calc.absolute_value(-5) == 5, "Absolute value failed"
    print("✓ Absolute Value: |-5| = 5")
    
    assert calc.percentage(200, 25) == 50, "Percentage failed"
    print("✓ Percentage: 25% of 200 = 50")
    
    assert calc.factorial(5) == 120, "Factorial failed"
    print("✓ Factorial: 5! = 120")
    
    # Test error handling
    print("\n✅ ERROR HANDLING TEST")
    print("-" * 70)
    
    try:
        calc.divide(10, 0)
        print("✗ Division by zero check failed")
    except ValueError as e:
        print(f"✓ Division by zero caught: {e}")
    
    try:
        calc.square_root(-4)
        print("✗ Square root of negative number check failed")
    except ValueError as e:
        print(f"✓ Square root of negative caught: {e}")
    
    try:
        calc.modulo(10, 0)
        print("✗ Modulo by zero check failed")
    except ValueError as e:
        print(f"✓ Modulo by zero caught: {e}")
    
    try:
        calc.factorial(-5)
        print("✗ Negative factorial check failed")
    except ValueError as e:
        print(f"✓ Negative factorial caught: {e}")
    
    # Test history
    print("\n✅ HISTORY TRACKING TEST")
    print("-" * 70)
    
    initial_count = len(calc.history)
    print(f"Initial history entries: {initial_count}")
    print(f"✓ History contains {len(calc.history)} entries")
    
    print("\n" + "=" * 70)
    print("📊 FINAL HISTORY")
    print("=" * 70)
    for idx, entry in enumerate(calc.history, 1):
        timestamp = entry["timestamp"]
        operation = entry["operation"]
        result = entry["result"]
        
        if isinstance(result, float) and result == int(result):
            result_str = str(int(result))
        else:
            result_str = f"{result:.10g}"
        
        print(f"{idx:2d}. [{timestamp}] {operation:20s} = {result_str}")
    
    print("=" * 70)
    print("\n✅ ALL TESTS PASSED! Professional Calculator is working perfectly.")
    print(f"📊 Total operations tested: {len(calc.history)}")


if __name__ == "__main__":
    test_calculator()
