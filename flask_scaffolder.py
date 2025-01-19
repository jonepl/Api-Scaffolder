import os
from pathlib import Path

VS_CODE_CONTENT = """{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Flask Debugger",
      "type": "debugpy",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "app/api.py",
        "FLASK_DEBUG": "1"
      },
      "args": [
        "run",
        "--no-debugger",
        "--no-reload"
      ],
      "jinja": true,
      "autoStartBrowser": false,
      "purpose": ["debug-in-terminal"]
    },
    {
      "name": "Pytest Debugger",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      // "args": ["-sv", "tests/e2e/test_api.py"],
      "console": "integratedTerminal"
    },
  ]
}"""

REQUIREMENTS_TXT = """# Application Dependencies
Flask==2.3.2
Flask-Cors==3.0.10
pytest==8.1.1
python-dotenv==0.14.0
 
# Testing Dependencies
pytest-cov==5.0.0
flake8==7.0.0
flake8-black==0.3.6
"""

PYTEST_INI = """[pytest]
pythonpath = .
"""

GITIGNORE = """# Ignore virtual environment files
venv/

# Ignore API scaffolder
api_scaffolder.py

# log files
app/logger/files
"""

FLAKE8 = """[flake8]
max-line-length = 106
exclude = 
    .git,
    __pycache__,
    venv,
    env
ignore = E402, E203, W503
plugins = flake8-black
"""

LOGGER_APP_LOGGER = """import logging
import logging.config
from dotenv import load_dotenv

from app.logger.helpers import get_config, create_log_file

# Load environment variables
load_dotenv()


def setup_logging():
    \"""Setup logging configuration.\"""

    # Load logging configuration
    config = get_config()

    # Ensure log file exists
    create_log_file(config)

    # Configure logging
    logging.config.dictConfig(config)
"""

LOGGER_CONFIG = """from app.logger.constants import APPLICATION_PATH

test_config = {
    "version": 1,
    "root": {"level": "INFO", "handlers": ["wsgi", "file"]},
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "default",
        },
        "file": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": f"{APPLICATION_PATH}/logger/files/test.log",
        },
    },
    "formatters": {
        "default": {
            "format": "%(asctime)s.%(msecs)03d:%(name)s:%(levelname)s:%(message)s",
            "datefmt": "%m-%d-%Y %I:%M:%S",
        }
    },
}

dev_config = {
    "version": 1,
    "root": {"level": "INFO", "handlers": ["wsgi", "file"]},
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "default",
        },
        "file": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": f"{APPLICATION_PATH}/logger/files/dev.log",
        },
    },
    "formatters": {
        "default": {
            "format": "%(asctime)s.%(msecs)03d:%(name)s:%(levelname)s:%(message)s",
            "datefmt": "%m-%d-%Y %I:%M:%S",
        }
    },
}

prod_config = {
    "version": 1,
    "root": {"level": "INFO", "handlers": ["wsgi", "file"]},
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "default",
        },
        "file": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": f"{APPLICATION_PATH}/logger/files/app.log",
        },
    },
    "formatters": {
        "default": {
            "format": "%(asctime)s.%(msecs)03d:%(name)s:%(levelname)s:%(message)s",
            "datefmt": "%m-%d-%Y %I:%M:%S",
        }
    },
}
"""

LOGGER_CONSTANTS = """import os
from enum import Enum

APPLICATION_DIR = "app"
APPLICATION_ROOT = os.getcwd()
APPLICATION_PATH = f"{APPLICATION_ROOT}/{APPLICATION_DIR}"


class AppEnv(Enum):
    DEV = "DEV"
    PROD = "PROD"
    STAGING = "STAGING"
    TEST = "TEST"


APP_ENV_NAME = "APP_ENV"
ROOT_LOGGER_NAME = "root"
FILE_HANDLER_KEY = "file"
FILENAME_KEY = "filename"
HANDLERS_KEY = "handlers"
"""

LOGGER_HELPER = """import os

import app.logger.config as loggerConfig
from app.logger.constants import (
    AppEnv,
    FILE_HANDLER_KEY,
    FILENAME_KEY,
    HANDLERS_KEY,
    APP_ENV_NAME,
)


def get_config():
    env = os.environ.get(APP_ENV_NAME)

    if env == AppEnv.DEV.value:
        config = loggerConfig.dev_config
    elif env == AppEnv.PROD.value:
        config = loggerConfig.prod_config
    elif env == AppEnv.TEST.value:
        config = loggerConfig.test_config
    elif env == AppEnv.STAGING.value:
        config = loggerConfig.prod_config
    else:
        config = loggerConfig.dev_config

    return config


def create_log_file(config: dict):
    dirName = os.path.dirname(
        config.get(HANDLERS_KEY).get(FILE_HANDLER_KEY).get(FILENAME_KEY)
    )
    os.makedirs(dirName, exist_ok=True)
"""

MODEL = """import logging

logger = logging.getLogger(__name__)


def get_data():
    logger.info("Fetching data in my_model.py")
"""

ROUTES = """import logging
from flask import jsonify
from flask_cors import cross_origin

logger = logging.getLogger(__name__)


def configure_routes(app):
    @app.route("/api/health", methods=["GET"])
    @cross_origin()
    def health():
        logger.info("Received health GET request")
        resp = jsonify({"message": "SUCCESS"})
        resp.status_code = 200
        return resp
"""

SERVICES_CONTENT = """import logging

logger = logging.getLogger(__name__)


def perform_service_task():
    logger.info("Performing a service task in my_services.py")
"""

API_CONTENT = """from flask import Flask
from app.logger.app_logger import setup_logging

setup_logging()

from app.routes.routes import configure_routes

app = Flask(__name__)
app.logger.info("Starting API ...")

configure_routes(app)

if __name__ == "__main__":
    app.run()
"""

TESTS_E2E_CONTENT = """import pytest

from app.api import app as flask_app


@pytest.fixture()
def client():
    flask_app.testing = True
    with flask_app.test_client() as client:
        yield client


def test_root(client):
    \"""Test the root endpoint ('/') for a 'hello world' message.\"""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json == {"message": "SUCCESS"}
"""

README_CONTENT = """# Read Me

## Environment Setup

### 1. Create python virtual environment within the server directory

#### Mac

```bash
   $ python -m venv venv 
   
   # OR
   make create-venv
```

#### Windows

```bash
   py -3 -m venv venv
```

### 2. Startup the virtual environment

#### Mac

```bash
   $ . venv/bin/activate
   
   # OR
   make activate-venv
```

#### Windows

```bash
   $ {path/to/project/folder}/venv/Scripts/activate
```

### 3. Install python dependencies

While venv is activated execute the following command

#### Mac

```bash
   $ pip install -r requirements.txt

   # OR
   make install
```

#### Windows

```bash
   pip install -r requirements.txt #make sure your python version is compatible with packages in .txt file
   pip install flask
```

### 4. Shutting down venv

Navigate within the server directory

#### Mac & Windows

```bash
$ deactivate

# OR
$ make deactivate-venv
```

## Usage

### Defining Environment Variables

You can set the `APP_ENV` environment variable to to initialize the application state:
  * DEV (DEFAULT)
  * PROD
  * STAGING
  * TEST

### Starting API

```bash
$ python -m app.api

# OR
$ make start
```

### Running tests
```bash
$ pytest

# OR
$ make test
```

### Linting & Formating

```bash
# Lint
$ flake8 .

# OR
$ make lint
```

```bash
# Format
$ black .

# OR
$ make format
```"""

MAKEFILE = """create-venv:
	python3 -m venv venv

activate-venv:
	. venv/bin/activate

deactivate-venv:
	. venv/bin/deactivate

install:
	venv/bin/pip install -r requirements.txt

start:
	venv/bin/python -m app.api

test:
	pytest

lint:
	flake8 .

format:
	black ."""

# Define the folder structure and file content
FOLDER_STRUCTURE = {
    ".vscode": {
        "launch.json": VS_CODE_CONTENT,
    },
    "app": {
        "logger":  {
            "app_logger.py": LOGGER_APP_LOGGER,
            "config.py": LOGGER_CONFIG,
            "constants.py": LOGGER_CONSTANTS,
            "helpers.py": LOGGER_HELPER,
        },
        "models": {
            "my_model.py": MODEL,
        },
        "routes": {
            "routes.py": ROUTES,
        },
        "services": {
            "my_services.py": SERVICES_CONTENT,
        },
        "api.py": API_CONTENT,
    },
    "tests": {
        "e2e": {
            "test_e2e.py": TESTS_E2E_CONTENT
        },
        "integration": {},
        "unit": {},
    },
    ".flake8": FLAKE8,
    ".gitignore": GITIGNORE,
    "pytest.ini": PYTEST_INI,
    "README.md": README_CONTENT,
    "requirements.txt": REQUIREMENTS_TXT,
    "Makefile": MAKEFILE
}

# Function to create the folder structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = Path(base_path) / name
        if isinstance(content, dict):
            # Create a directory and recurse
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, str):
            # Create a file and write content
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w") as f:
                f.write(content)
        elif content is None:
            # Create an empty directory
            path.mkdir(parents=True, exist_ok=True)

# Main function
def main():
    base_path = os.path.dirname(os.path.realpath(__file__))
    os.makedirs(base_path, exist_ok=True)


    create_structure(base_path, FOLDER_STRUCTURE)
    print(f"Project scaffolded at: {base_path}")

if __name__ == "__main__":
    main()
