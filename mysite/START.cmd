@echo off
setlocal
cd /d "%~dp0"
set "DJANGO_SETTINGS_MODULE=mysite.settings"
python -m django --version >nul 2>&1
if errorlevel 1 (
    echo Django was not found. Run: python -m pip install -r requirements.txt
    pause
    exit /b 1
)
python -B prepare_catalog.py
if errorlevel 1 (
    pause
    exit /b 1
)
echo Open http://127.0.0.1:8011/ in your browser.
python -B manage.py runserver 127.0.0.1:8011 --noreload
if errorlevel 1 pause
