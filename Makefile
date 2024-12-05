run:
	poetry run python advent_of_code_2024/day$(day)/part$(part).py

test:
	poetry run pytest

lint:
	poetry run ruff check --fix

format:
	poetry run ruff format advent_of_code_2024
