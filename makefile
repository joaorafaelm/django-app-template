.PHONY:
.ONESHELL:

-include .env
export

all: help

help: # show all commands
	@sed -n 's/:.#/:/p' makefile | grep -v @

venv: # create virtual environment
	@uv venv --allow-existing --quiet

sync: venv # install dependencies
	@uv sync

lint: # lint all files
	@uv run ruff check --fix
	@uv run ruff format

test: # run tests
	@uv run pytest

migrations: # create migrations
	@uv run python manage.py makemigrations --no-header

migrate: # apply migrations
	@uv run python manage.py migrate

run: # run app
	@uv run python manage.py runserver
