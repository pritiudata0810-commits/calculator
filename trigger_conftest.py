#!/usr/bin/env python
"""Import conftest to trigger test file creation."""
import sys
import os

# Change to the calculator directory
os.chdir(r'D:\calculator\calculator')
sys.path.insert(0, r'D:\calculator\calculator')

# Import conftest.py to execute its setup code
import conftest

# Verify the files were created
tests_dir = r'D:\calculator\calculator\tests'
print("\n" + "=" * 70)
print("VERIFICATION - Test Files Created via Conftest")
print("=" * 70)
print(f"\nDirectory: {tests_dir}")
print(f"Directory exists: {os.path.exists(tests_dir)}")

if os.path.exists(tests_dir):
    print(f"\nFiles created:")
    files = sorted(os.listdir(tests_dir))
    for file in files:
        fpath = os.path.join(tests_dir, file)
        if os.path.isfile(fpath):
            size = os.path.getsize(fpath)
            print(f"  {file:<30} {size:>8} bytes")
    print(f"\nTotal files: {len(files)}")
    print("\n✓ Test files setup completed successfully!")
else:
    print("\nERROR: Tests directory was not created")
