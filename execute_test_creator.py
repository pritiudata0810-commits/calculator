#!/usr/bin/env python3
"""
Execute the create_tests_dir.py script and capture all output.
"""

import subprocess
import sys
import os

os.chdir('D:\\calculator\\calculator')

print("=" * 60)
print("EXECUTING: python create_tests_dir.py")
print("=" * 60)
print()

# Run the create_tests_dir.py script
result = subprocess.run([sys.executable, 'create_tests_dir.py'], capture_output=True, text=True)

# Print the output
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)

print()
print("=" * 60)
print("VERIFICATION: Checking created files and directory")
print("=" * 60)
print()

# Verify the directory was created
tests_dir = 'D:\\calculator\\calculator\\tests'
if os.path.exists(tests_dir):
    print(f"✓ Tests directory exists: {tests_dir}")
else:
    print(f"✗ Tests directory NOT found: {tests_dir}")
    sys.exit(1)

# List the contents
print("\nContents of tests directory:")
if os.path.isdir(tests_dir):
    for item in os.listdir(tests_dir):
        item_path = os.path.join(tests_dir, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"  ✓ {item} ({size} bytes)")
        else:
            print(f"  ✓ {item}/ (directory)")

# Verify specific files
print("\nFile verification:")
init_file = os.path.join(tests_dir, '__init__.py')
test_file = os.path.join(tests_dir, 'test_calculator.py')

if os.path.exists(init_file):
    print(f"  ✓ {init_file} exists")
else:
    print(f"  ✗ {init_file} NOT found")

if os.path.exists(test_file):
    size = os.path.getsize(test_file)
    print(f"  ✓ {test_file} exists ({size} bytes)")
    # Show first few lines
    with open(test_file, 'r') as f:
        lines = f.readlines()[:5]
        print(f"    First few lines of test_calculator.py:")
        for line in lines:
            print(f"      {line.rstrip()}")
else:
    print(f"  ✗ {test_file} NOT found")

print()
print("=" * 60)
print("SETUP COMPLETE")
print("=" * 60)
