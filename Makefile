.PHONY=venv, clean, install, set-cookie, lint, format, test
SHELL:=/bin/bash

venv:
	python3 -m venv venv

clean:
	rm -rf .ipynb_checkpoints
	rm -rf **/.ipynb_checkpoints
	rm -rf .pytest_cache
	rm -rf **/.pytest_cache
	rm -rf __pycache__
	rm -rf **/__pycache__
	rm -rf build
	rm -rf dist

install: venv
	source venv/bin/activate; pip install -r requirements.txt

set-cookie: venv
	source venv/bin/activate; python runner.py set-cookie

lint:
	source venv/bin/activate; ruff .

format:
	source venv/bin/activate; black .
	source venv/bin/activate; ruff . --fix

test:
	source venv/bin/activate; pytest .
