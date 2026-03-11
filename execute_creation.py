if __name__ == '__main__':
    import os
    import sys
    os.chdir(r'D:\calculator\calculator')
    sys.path.insert(0, r'D:\calculator\calculator')
    from create_tests_direct import create_test_files
    create_test_files()
