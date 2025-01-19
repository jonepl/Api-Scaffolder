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
- Modular and scalable folder structure.
- Pre-configured logging with customizable levels.
- Built-in support for unit and integration testing using `pytest`.
- Configurable environments (DEV, STAGING, PROD).
- Linting and formatting with `flake8` and `black`.
- Support for CORS, database integration, and error handling.


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jonepl/flask-scaffolder.git
   ```

## Usage
Scaffold the flask API with the following steps

```
$ python flask_scaffolder.py
```


---

## Project Structure
- Describe the default folder structure created by the scaffolder.
- Explain the purpose of key files and directories.

**Example**:
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
├── pytest.ini
├── README.md                 # Detailed Applicatio Instructions 
└── requirements.txt
```

## Acknowledgments

- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- `black` code formatter: [https://github.com/psf/black](https://github.com/psf/black)
- `pytest` testing framework: [https://pytest.org/](https://pytest.org/)
