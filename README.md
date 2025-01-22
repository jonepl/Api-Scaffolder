# Flask API Scaffolder

## Table of Contents
1. [Project Title and Description](#project-title-and-description)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Acknowledgments](#acknowledgments)


## Project Title and Description
A tool to quickly scaffold Python Flask applications with pre-configured settings for routing, logging, testing, and deployment. Simplify your Flask project setup and get started with minimal effort.

## Features
- **Modular and Scalable Folder Structure:** Easily extend the application with a well-organized and maintainable structure.
- **Pre-configured Logging:** Customizable logging levels for better debugging and monitoring.
- **Built-in Testing Support:** Unit, integration, and end-to-end testing with `pytest`.
- **Configurable Environments:** Seamlessly switch between DEV, STAGING, and PROD environments.
- **Linting and Formatting:** Code quality ensured with `flake8` for linting and `black` for consistent formatting.
- **Dockerized Deployment:** A ready-to-use `Dockerfile` to containerize the API for streamlined deployment and consistency across environments.


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jonepl/flask-scaffolder.git
   ```

## Usage
Scaffold the flask API with the following steps

```bash
# Scaffolds a new API using absolute path
$ python flask_scaffolder.py -p /Users/name/Projects/my-app --absolute

# Scaffolds a new API using relative path
$ python flask_scaffolder.py -p my-app --relative
```

## Project Structure

```markdown
## Project Structure

my-flask-app/
├── .vscode                    # Flask and Pytest Debgger configuration
├── app
│  ├── logger
│  │  ├── app_logger.py        
│  │  ├── config.py
│  │  ├── constants.py
│  │  └── helpers.py
│  ├── models
│  │  └── my_model.py          # Sample model
│  ├── routes
│  │  └── routes.py            # Modular route definitions
│  ├── services
│  │  └── my_services.py       # Sample service
│  └── api.py                  # Application entry point
├── tests
│  ├── e2e
│  │  └── test_e2e.py
│  ├── integration
│  └── unit
└── .flake8
├── .gitignore
├── Makfile                   # Convient applicaiton commands
├── Dockerfile                # Dockerfile for containerizing you API
├── pytest.ini
├── README.md                 # Detailed Applicatio Instructions 
└── requirements.txt
```

## Acknowledgments

- `flask` api: https://flask.palletsprojects.com/
- `black` code formatter: https://black.readthedocs.io/en/stable/
- `flake8` linter: https://flake8.pycqa.org/en/latest/index.html
- `pytest` testing framework: https://pytest.org/
- `gunicorn` WSGI HTTP Server: https://gunicorn.org/#docs
