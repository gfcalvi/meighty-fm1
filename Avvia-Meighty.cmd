@echo off
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
 py -3 Avvia-Meighty.py
) else (
 python Avvia-Meighty.py
)
pause
