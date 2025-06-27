DynamoDB Control Plane Project
What’s included:

Streamlit application for working with DynamoDB

Unit tests using pytest + moto

Virtual environment (venv) setup (manual installation)

Batch scripts for easy execution

 How to run the project


1️⃣ Set up the virtual environment

Easy way and main 1:
run in terminal:

pip install .
If it's not working:

Run:

install_venv.bat

It will:

create the venv directory

upgrade pip

install dependencies from requirements.txt

If you encounter issues, install manually:

venv\Scripts\python.exe -m pip install -r requirements.txt

or!
pip install streamlit boto3 pandas pytest moto==4.2.12


2️⃣ Start the Streamlit app
Run:
start.bat
If it doesn’t open automatically, run manually:
python -m streamlit run app.py


3️⃣ Run the tests
Run:
start_tests_venv.bat

Or manually:
venv\Scripts\activate
python -m pytest tests

⚙️ Important dependencies
moto==4.2.12 → fixes compatibility with mock_dynamodb

pytest → for running unit tests

streamlit → for the interactive interface