#!/usr/bin/env python3
"""Execute the final_test_setup.py script directly."""
import subprocess
import sys
import os

os.chdir(r'D:\calculator\calculator')
result = subprocess.run([sys.executable, 'final_test_setup.py'], capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print(result.stderr, file=sys.stderr)
sys.exit(result.returncode)
