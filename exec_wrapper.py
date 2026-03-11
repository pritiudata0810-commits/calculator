"""
Execution wrapper - imports and executes master_setup
"""
import sys
import os

# Ensure we're in the right directory
os.chdir(r'D:\calculator\calculator')

if __name__ == '__main__':
    # Import the master setup module
    import master_setup
    # This will execute the main() function when master_setup is imported
    sys.exit(0)
