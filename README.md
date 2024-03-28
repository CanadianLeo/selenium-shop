# Selenium test repo

## Dependencies
- Python +3.9.*
- Selenium +4.18.*
- Chrome web driver (for your browser)

## Quick start

### Create env
Use the command for creating python enviroment
```bash
python3 -m venv selenium_env
source selenium_env/bin/activate
```

### Install dependencies
Use the command for install dependencies
```bash
pip install -r "requirements.txt"
```

### Run any of script
Use the command for run the script
```bash
pytest test_items.py # for ru language
pytest --language=es test_items.py # for es language
pytest --language=fr test_items.py # for fr language
```