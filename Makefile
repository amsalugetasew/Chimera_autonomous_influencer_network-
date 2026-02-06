.PHONY: setup test spec-check

setup:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest -q

spec-check:
	# Optional: Check if code matches specs
	python scripts/spec_checker.py
