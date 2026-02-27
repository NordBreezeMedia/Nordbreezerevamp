@echo off
title Nord Breeze Media - Local Server
echo.
echo  Starting local server...
echo  Open in your browser:  http://localhost:8080
echo  Press Ctrl+C to stop the server.
echo.
cd /d "%~dp0"
python -m http.server 8080
pause
