# Simple GET Endpoint (FastAPI)

This project contains a simple GET endpoint implemented with **FastAPI**,  
a linter (**ruff**), and automatic tests using **pytest**.  
The project follows a clean structure using the `src/` folder layout.

---

## ✅ Features
- FastAPI GET endpoint returning a greeting message  
- Linter: **ruff**  
- Automatic tests: **pytest**  
- `.gitignore` included  
- Clean project structure (`src/quiz_bot`)  
- Uses **uv** for environment & dependency management  

---

## ▶️ Run the application

```bash
uv run uvicorn quiz_bot.main:app --reload
🧪 Run tests
bash

uv run pytest -q
Expected output:


1 passed
📁 Project Structure
css

quiz-bot/
 ├── src/
 │   └── quiz_bot/
 │        ├── __init__.py
 │        └── main.py
 ├── tests/
 │   └── test_main.py
 ├── .gitignore
 ├── pyproject.toml
 ├── README.md
✨ Technologies Used
FastAPI

uv

pytest

ruff

👩‍💻 Author
Feyza Balaban
