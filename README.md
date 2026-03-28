# DevOps Workflow for Python Streamlit Application

This project demonstrates a complete DevOps workflow for a Python Streamlit application, including:

- Source control with Git and GitHub
- Automated testing and linting (CI/CD)
- Dependency management
- Code quality enforcement
- Containerization with Docker
- Example deployment scripts
- Documentation

## Project Structure

- `src/` — Application source code (Streamlit app)
- `tests/` — Unit tests
- `.github/workflows/` — CI/CD pipeline (GitHub Actions)
- `requirements.txt` — Python dependencies
- `Dockerfile` — Containerization
- `Makefile` — Common DevOps tasks
- `deploy.sh` / `deploy.ps1` — Example deployment scripts

## Quick Start

### Local Development
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run Streamlit app:
   ```sh
   streamlit run src/app.py
   ```
3. Run tests:
   ```sh
   pytest
   ```
4. Lint and format code:
   ```sh
   flake8 .
   black --check .
   ```

### Docker
1. Build Docker image:
   ```sh
   docker build -t python-devops-app .
   ```
2. Run in Docker:
   ```sh
   docker run -p 8501:8501 python-devops-app
   ```
3. Open [http://localhost:8501](http://localhost:8501) in your browser.

### CI/CD
On every push or pull request to `main`, the workflow runs linting, formatting, and tests automatically.

---

## License
MIT
