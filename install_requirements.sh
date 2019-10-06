# USE THIS SCRIPT TO SETUP THE PYTHON ENVIRONMENT
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
deactivate
cd application
touch key.json
