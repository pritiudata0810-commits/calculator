if __name__ == '__main__':
    import subprocess
    import sys
    result = subprocess.run([sys.executable, 'setup_tests.py'], cwd='D:/calculator/calculator')
    sys.exit(result.returncode)
