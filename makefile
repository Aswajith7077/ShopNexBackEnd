.PHONY: format format-black format-isort check check-black check-isort

# Directories to include (excluding .venv)
SRC_DIRS := app models services scripts config

format: format-black format-isort

format-black:
	black $(SRC_DIRS)

format-isort:
	isort $(SRC_DIRS)

check: check-black check-isort

check-black:
	black --check $(SRC_DIRS)

check-isort:
	isort --check-only $(SRC_DIRS)
