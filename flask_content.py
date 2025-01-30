API_CONTENT = """from flask import Flask
from logger.app_logger import setup_logging

setup_logging()

from routes.routes import configure_routes

app = Flask(__name__)
app.logger.info("Starting API ...")

configure_routes(app)

if __name__ == "__main__":
    app.run()
"""

APP_CONSTANTS = """EXAMPLE_CONSTANTS="consts"
"""

DOCKERFILE = """FROM python:3.8-slim

WORKDIR /app

# Download Libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app into working directory
COPY ./app .

# Expose ports
EXPOSE 8080

# Start application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "api:app"]
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

GITIGNORE = """# Ignore virtual environment files
venv/

# Ignore API scaffolder
api_scaffolder.py

# log files
app/logger/files
"""

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
Flask-Pydantic==0.12.0

# Dev Ops Dependencies
gunicorn==22.0.0
 
# Testing Dependencies
pytest-cov==5.0.0
flake8==7.0.0
flake8-black==0.3.6
"""

PYTEST_INI = """[pytest]
pythonpath = .
"""

LOGGER_APP_LOGGER = """import logging
import logging.config
from dotenv import load_dotenv

from logger.helpers import get_config, create_log_file

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

LOGGER_CONFIG = """from logger.constants import APPLICATION_PATH

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

import logger.config as loggerConfig
from logger.constants import (
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

MAKEFILE = """build-image:
	docker build -t my-api:latest .

create-venv:
	python3 -m venv venv

activate-venv:
	. venv/bin/activate

deactivate-venv:
	. venv/bin/deactivate

install:
	venv/bin/pip install -r requirements.txt

start:
	venv/bin/python app/api.py

test:
	pytest

lint:
	flake8 .

format:
	black ."""

MODEL = """from typing import Optional
from pydantic import BaseModel


class QueryModel(BaseModel):
    age: int


class ResponseModel(BaseModel):
    id: int
    age: int
    name: str
    nickname: Optional[str] = None


class RequestBodyModel(BaseModel):
    name: str
    nickname: Optional[str] = None


class RequestFormDataModel(BaseModel):
    name: str
    nickname: Optional[str] = None

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
# Starting API Locally
$ python app/api.py

# OR
$ make start
```

### Starting API via Docker Image
```bash
$ docker build -t my-api:latest .

docker run -d \
  --name my-api \
  --expose 8080 \
  -p 8080:8080 \
  my-api:latest
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

ROUTES = """import logging
from flask import jsonify
from flask_cors import cross_origin
from flask_pydantic import validate

from models.my_model import (
    ResponseModel,
    RequestBodyModel,
    RequestFormDataModel,
    QueryModel,
)

logger = logging.getLogger(__name__)


def configure_routes(app):
    @app.route("/api/health", methods=["GET"])
    @cross_origin()
    def health():
        logger.info("Received health GET request")
        resp = jsonify({"message": "SUCCESS"})
        resp.status_code = 200
        return resp

    # Example query
    @app.route("/api/users", methods=["GET"])
    @validate()
    def get_user(query: QueryModel):
        age = query.age
        response = ResponseModel(id=1, age=age, name="John Doe")
        return response

    # Example URL path
    @app.route("/api/users/<user_id>/", methods=["GET"])
    @validate()
    def get_character(user_id: int):
        characters = [
            ResponseModel(id=1, age=95, name="Geralt", nickname="White Wolf"),
            ResponseModel(id=2, age=45, name="Triss Merigold", nickname="sorceress"),
            ResponseModel(
                id=3, age=42, name="Julian Alfred Pankratz", nickname="Jaskier"
            ),
            ResponseModel(id=4, age=101, name="Yennefer", nickname="Yenn"),
        ]
        try:
            return characters[user_id]
        except IndexError:
            return {"error": "Not found"}, 400

    # Example request body
    @app.route("/api/users/", methods=["POST"])
    @validate()
    def post(body: RequestBodyModel):
        name = body.name
        nickname = body.nickname
        return ResponseModel(name=name, nickname=nickname, id=0, age=1000)

    # Example form data
    @app.route("/api/users/formdata/", methods=["POST"])
    @validate()
    def post_formdata(form: RequestFormDataModel):
        name = form.name
        nickname = form.nickname
        return ResponseModel(name=name, nickname=nickname, id=0, age=1000)

"""

SERVICES_CONTENT = """import logging

logger = logging.getLogger(__name__)


def perform_service_task():
    logger.info("Performing a service task in my_services.py")
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
