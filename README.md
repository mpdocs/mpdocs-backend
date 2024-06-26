# drf_template
Template of a Python service that uses Django-REST framework with poetry. Build, test and CI scripts ready.

## Usage

### Create virtual environment

```bash
python -m virtualenv --python=3.12 venv
```

Activate venv

🔑 Copy `.env.example` to `.env` and change api settings

### Install dependencies

* 🐍 Install poetry with command `pip install poetry`
* 📎 Install dependencies with command `poetry install`

### Install pre-commit hooks

To install pre-commit simply run inside the shell:

```bash
pre-commit install
```

To run it on all of your files, do

```bash
pre-commit run --all-files
```


### Apply migrations

🎓 Run  `python manage.py migrate`

### Run project

🚀 Run project via `python manage.py runserver`

Run celery worker:

```bash
celery -A service worker -l INFO`or via `celery -A service worker -l INFO
```

[//]: # ( -P eventlet)

Run celery scheduler:

```bash
celery -A service beat
```

### Generate openapi schema

```bash
python manage.py spectacular --color --file ./docs/api/schema.yml
```