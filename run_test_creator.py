#!/usr/bin/env python3
"""
Wrapper script to run the test structure creator directly.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, r'D:\calculator\calculator')

# Import and run the test creator function
try:
    from create_tests_structure import create_tests_structure
    create_tests_structure()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
