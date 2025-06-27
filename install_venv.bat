@echo off
chcp 65001
cd /d %~dp0

echo === Creating virtual environment ===
python -m venv venv

echo === Upgrading pip ===
venv\Scripts\python.exe -m pip install --upgrade pip

echo === Installing requirements ===
venv\Scripts\python.exe -m pip install -r requirements.txt

echo === Installed packages ===
venv\Scripts\python.exe -m pip list

echo === Checking pytest ===
venv\Scripts\python.exe -m pytest --version
if errorlevel 1 (
    echo ❌ pytest not installed properly!
    pause
    exit /b
)

echo ✅ Setup complete. You can now run tests using start_tests_venv.bat
pause
