"""Verification script to confirm test directory structure was created."""
import os
import sys

# Add the calculator directory to the path
sys.path.insert(0, 'D:\\calculator\\calculator')

# Import conftest to trigger directory creation
import conftest

# Verify the structure
tests_dir = 'D:\\calculator\\calculator\\tests'
init_file = os.path.join(tests_dir, '__init__.py')
test_file = os.path.join(tests_dir, 'test_calculator.py')

print("=" * 60)
print("VERIFICATION REPORT")
print("=" * 60)

# Check directory
if os.path.isdir(tests_dir):
    print(f"✓ Tests directory created: {tests_dir}")
else:
    print(f"✗ Tests directory NOT found: {tests_dir}")
    sys.exit(1)

# Check __init__.py
if os.path.isfile(init_file):
    size = os.path.getsize(init_file)
    print(f"✓ __init__.py created: {init_file} ({size} bytes)")
else:
    print(f"✗ __init__.py NOT found: {init_file}")
    sys.exit(1)

# Check test_calculator.py
if os.path.isfile(test_file):
    size = os.path.getsize(test_file)
    with open(test_file, 'r') as f:
        content = f.read()
        line_count = len(content.split('\n'))
    print(f"✓ test_calculator.py created: {test_file}")
    print(f"  - File size: {size} bytes")
    print(f"  - Lines: {line_count}")
    
    # Count test cases
    test_count = content.count('def test_')
    print(f"  - Test cases: {test_count}")
    
    # Verify essential test classes
    classes = ['TestBasicOperations', 'TestAddition', 'TestSubtraction', 
               'TestMultiplication', 'TestDivision', 'TestEdgeCases']
    found_classes = []
    for cls in classes:
        if f'class {cls}' in content:
            found_classes.append(cls)
    
    if found_classes:
        print(f"  - Test classes found: {', '.join(found_classes)}")
else:
    print(f"✗ test_calculator.py NOT found: {test_file}")
    sys.exit(1)

print("=" * 60)
print("SUCCESS: All test files and directories created!")
print("=" * 60)
print("\nYou can now run:")
print("  pytest D:\\calculator\\calculator\\tests")
print("  or")
print("  pytest D:\\calculator\\calculator")
