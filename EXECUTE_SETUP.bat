@echo off
REM Execute the test setup script
REM This batch file will create the tests directory and all test files

cd /d D:\calculator\calculator

echo Creating test directory structure...
python final_test_setup.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo SUCCESS: Test directory created!
    echo ========================================
    echo.
    dir tests /b
) else (
    echo.
    echo ERROR: Setup failed with code %ERRORLEVEL%
    echo.
    echo Trying alternative Python path...
    py final_test_setup.py
)

pause
