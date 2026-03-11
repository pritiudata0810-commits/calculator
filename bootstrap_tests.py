#!/usr/bin/env python3
"""Bootstrap script that ensures test directory structure exists."""
import os
import sys

# Make sure we're in the right directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Execute the setup_tests.py script
sys.path.insert(0, script_dir)
from setup_tests import main

# Run the setup
try:
    main()
    print("\n" + "="*50)
    print("SUCCESS: Test directory structure created!")
    print("="*50)
    
    # Verify the files exist
    tests_dir = os.path.join(script_dir, 'tests')
    if os.path.isdir(tests_dir):
        files = os.listdir(tests_dir)
        print(f"\nDirectory contents: {files}")
        print(f"✓ Tests directory: {os.path.abspath(tests_dir)}")
        
        for f in files:
            file_path = os.path.join(tests_dir, f)
            size = os.path.getsize(file_path)
            print(f"  ✓ {f} ({size} bytes)")
    
    sys.exit(0)
except Exception as e:
    print(f"\nERROR: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit(1)
