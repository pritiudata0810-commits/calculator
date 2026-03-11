import subprocess
import sys

result = subprocess.run([sys.executable, 'D:\\calculator\\calculator\\create_tests_dir.py'])
sys.exit(result.returncode)
