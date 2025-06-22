.PHONY: install test format lint

install:
	pip install -r requirements.txt
	playwright install chromium

test:
	pytest tests/

format:
	black src/ tests/

lint:
	flake8 src/ tests/