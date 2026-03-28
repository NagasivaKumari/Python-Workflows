# 🚀 DevOps Workflow for Python Applications

## 📌 Overview

This project demonstrates a complete DevOps workflow for Python applications, showcasing how code is developed, validated, and automatically deployed using CI/CD practices.

The workflow is designed to be **framework-agnostic**, and a Streamlit application is used as an example implementation.

---

## 🔗 Live Application

👉 https://nagasivakumari-python-workflows-srcapp-bpsero.streamlit.app/
---

## 🧱 Project Structure

```text id="p1a9x3"
project/
│── src/                 # Application source code
│   └── app.py
   # Example Python application (Streamlit)
│
│── tests/               # Unit tests
│   └── test_app.py
│
│── .github/workflows/   # CI pipeline
│   └── python-app.yml
│
│── requirements.txt     # Dependencies
│── Dockerfile           # Containerization (optional)
│── Makefile             # Automation commands
│── README.md            # Documentation
```

---

## ⚙️ DevOps Workflow (CI/CD)

This project implements a complete CI/CD pipeline using GitHub Actions and Streamlit Cloud.

### 🔁 Workflow Steps

1. Developer pushes code to GitHub
2. A Pull Request is created
3. CI pipeline is triggered using GitHub Actions:

   * Install dependencies
   * Lint code using `flake8`
   * Check formatting using `black`
   * Run tests using `pytest`
4. If all checks pass:

   * Code is merged into the `main` branch
5. Continuous Deployment (CD):

   * Streamlit Cloud automatically detects changes
   * The latest version of the application is deployed
6. Updated application is available via live URL

---

## 🔧 Continuous Integration (CI)

Implemented using GitHub Actions:

* ✅ Automated dependency installation
* ✅ Code linting (`flake8`)
* ✅ Formatting check (`black`)
* ✅ Unit testing (`pytest`)

Ensures only validated code is merged into the main branch.

---

## 🚀 Continuous Deployment (CD)

Deployment is handled automatically using Streamlit Cloud:

* 🔄 Auto-deploy on every push to `main`
* 🚫 No manual deployment required
* 🌐 Instant updates to the live application

---

## 💻 Local Development

### Install dependencies

```bash id="ld1"
pip install -r requirements.txt
```

### Run the application

```bash id="ld2"
streamlit run src/app.py
```

### Run tests

```bash id="ld3"
pytest
```

### Lint and format check

```bash id="ld4"
flake8 .
black --check .
```

---

## 🧪 Technologies Used

* Python
* Streamlit
* Git & GitHub
* GitHub Actions (CI/CD)

---

## 📊 Key Features

* Automated CI pipeline
* Continuous deployment (CD)
* Clean and modular project structure
* Dependency management
* Code quality enforcement

---

## 📌 Notes

* This project demonstrates a generalized DevOps workflow applicable to Python applications.
* Streamlit is used as an example application for deployment.
* The CI/CD pipeline can be extended to other frameworks like Flask or FastAPI.

---

## 📄 License

MIT License

