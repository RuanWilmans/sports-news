\# Sports News (Django Capstone)



I kept the code simple and readable, added short docstrings, generated Sphinx

documentation, and included a Docker setup so it can run anywhere.



---



\## 🚀 Project Overview

This Django project is a simple \*\*Sports News web app\*\* that demonstrates the use of:

\- Django models, views, and templates

\- REST Framework for APIs

\- Automated documentation generation using \*\*Sphinx\*\*

\- Containerization with \*\*Docker\*\*



The main goal was to consolidate all the skills learned in the HyperionDev Software Engineering course into one deployable project.



---



\## 🧩 Setup \& Run (Virtual Environment)



Run the project locally using a Python virtual environment.



```bash

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver



