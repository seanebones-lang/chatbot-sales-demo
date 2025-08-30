@echo off
echo ========================================
echo    Islamic Study Guide - Auto Start
echo ========================================
echo.
echo Starting your Islamic Study Guide...
echo.
echo This will open in your web browser automatically.
echo.
echo If it doesn't open automatically:
echo 1. Copy this link: http://localhost:8080
echo 2. Paste it into your browser
echo.
echo Press any key to continue...
pause >nul

REM Try to open the application in the default browser
start http://localhost:8080

echo.
echo Application should now be opening in your browser!
echo.
echo If you see any errors, please let me know.
echo.
pause
