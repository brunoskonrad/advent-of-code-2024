run:
	poetry run python advent_of_code_2024/day$(day)/part$(part).py

lint:
	poetry run ruff check --fix
