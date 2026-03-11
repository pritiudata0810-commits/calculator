"""
This script demonstrates the setup that will occur when tests are run.
Import this module to trigger the test directory creation.
"""

def setup_and_verify():
    """Set up test structure and verify it was created."""
    import os
    
    # Setup the test directory structure
    import test_init
    
    tests_dir = r'D:\calculator\calculator\tests'
    
    print("=" * 70)
    print("VERIFICATION - Directory Contents with File Sizes")
    print("=" * 70 + "\n")
    
    abs_tests_dir = os.path.abspath(tests_dir)
    print(f"Directory Path: {abs_tests_dir}\n")
    
    # Display files with sizes
    print(f"{'Filename':<30} {'Size (bytes)':<15} {'Path'}")
    print("-" * 80)
    
    if os.path.exists(tests_dir):
        for filename in sorted(os.listdir(tests_dir)):
            filepath = os.path.join(tests_dir, filename)
            if os.path.isfile(filepath):
                size = os.path.getsize(filepath)
                abs_path = os.path.abspath(filepath)
                print(f"{filename:<30} {size:<15d} {abs_path}")
        
        # Summary statistics
        print("\n" + "=" * 70)
        print("SUMMARY")
        print("=" * 70)
        
        total_size = 0
        file_count = 0
        for filename in os.listdir(tests_dir):
            filepath = os.path.join(tests_dir, filename)
            if os.path.isfile(filepath):
                total_size += os.path.getsize(filepath)
                file_count += 1
        
        print(f"Total files created: {file_count}")
        print(f"Total size: {total_size} bytes")
        print(f"Directory exists: {os.path.isdir(tests_dir)}")
        print(f"Directory is readable: {os.access(tests_dir, os.R_OK)}")
        print(f"Directory is writable: {os.access(tests_dir, os.W_OK)}")
        print("\n✓ Test directory structure created successfully!")
        return True
    else:
        print("✗ Tests directory does not exist")
        return False

if __name__ == '__main__':
    import sys
    success = setup_and_verify()
    sys.exit(0 if success else 1)
