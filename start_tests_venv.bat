@echo off
chcp 65001
cd /d %~dp0

call venv\Scripts\activate
echo Running tests inside venv...
python -m pytest tests

pause
