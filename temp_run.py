#!/usr/bin/env python
"""Temporary wrapper to run final_create_tests.py"""
import os
import sys

# Change to the correct directory
os.chdir(r'D:\calculator\calculator')

# Execute the final_create_tests.py script
if __name__ == '__main__':
    with open('final_create_tests.py', 'r') as f:
        code = f.read()
    exec(code)
