.PHONY = venv, lint, test, clean

venv: venv/bin/activate
	python3 -m venv venv

install: venv
	source venv/bin/activate; pip install -r requirements.txt

set-cookie: venv
	source venv/bin/activate; python runner.py set-cookie

format:
	source venv/bin/activate; black .

test:
	source venv/bin/activate; pytest .
