@echo off
REM Simple batch script to set up tests directory

echo Creating test directory structure...

REM Change to script directory
cd /d "%~dp0"

REM Run Python setup
python auto_setup.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================
    echo Setup complete! You can now run:
    echo   pytest
    echo ====================================================
) else (
    echo Error during setup!
    exit /b 1
)
