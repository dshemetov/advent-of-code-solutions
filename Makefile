format:
	black .

test:
	pytest .
	python -m doctest -v ./*/**.py
