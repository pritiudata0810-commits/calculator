#!/usr/bin/env python3
"""
Minimal runner script that ensures test structure is created and runs pytest.
This imports conftest.py which triggers automatic test structure creation.
"""
import os
import sys
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to script directory
    os.chdir(script_dir)
    
    # Import conftest to trigger setup
    print("Initializing test structure...")
    try:
        import conftest
        print("✓ Test structure initialized")
    except Exception as e:
        print(f"Warning during initialization: {e}")
    
    # Verify structure was created
    tests_dir = os.path.join(script_dir, 'tests')
    if os.path.isdir(tests_dir):
        print(f"✓ Tests directory exists: {tests_dir}")
        
        init_file = os.path.join(tests_dir, '__init__.py')
        test_file = os.path.join(tests_dir, 'test_calculator.py')
        
        if os.path.isfile(init_file):
            print(f"✓ __init__.py exists")
        if os.path.isfile(test_file):
            size = os.path.getsize(test_file)
            print(f"✓ test_calculator.py exists ({size} bytes)")
    else:
        print(f"Note: Tests directory will be created on first pytest run")
    
    # Run pytest if available
    print("\nRunning pytest...")
    try:
        subprocess.run([sys.executable, '-m', 'pytest', '-v'], check=False)
    except Exception as e:
        print(f"Could not run pytest: {e}")
        print("You can run: pytest")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
