#!/usr/bin/env python3
import os
import sys

# Change to the calculator directory
os.chdir(r'D:\calculator\calculator')

# Add the current directory to path
sys.path.insert(0, os.getcwd())

# Import and run the setup
exec(open('final_test_setup.py').read())
