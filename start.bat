@echo off
chcp 65001
cd /d %~dp0

echo Activating virtual environment...
call venv\Scripts\activate

echo Starting Streamlit app...
python -m streamlit run Home.py

pause
