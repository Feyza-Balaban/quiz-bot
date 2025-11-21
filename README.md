# quiz-bot
Task 1 – Simple GET Endpoint

This project implements a simple FastAPI GET endpoint.
It returns a greeting message and includes development tools.

Features

Simple FastAPI GET endpoint (/)

Linter: ruff

Automatic test: pytest

Proper folder structure (src/quiz_bot)

.gitignore included

Uses uv for package & environment management

Run the application
uv run uvicorn quiz_bot.main:app --reload


Go to:
http://localhost:8000/

Run tests
uv run pytest -q