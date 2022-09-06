install:
	@pip install -e .
	@echo "Go to https://adventofcode.com/, inspect browser session, find the cookie."
	@read -p "Set your AoC token (n to skip): " TOKEN; \
		if [ $$TOKEN != "n" ]; then\
			echo "AOC_TOKEN='$$TOKEN'" > .env;\
		fi

format:
	black .

test:
	pytest .
