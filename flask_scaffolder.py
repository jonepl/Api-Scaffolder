import os
import click
from pathlib import Path

from flask_content import *

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
    "Dockerfile": DOCKERFILE,
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
@click.command()
@click.option("-p", "--path", required=True, type=click.Path(file_okay=False, writable=True, resolve_path=True), help="The base directory where the project should be scaffolded.")
@click.option("-a", "--absolute", is_flag=True, help="Specify that the provided path is absolute.")
@click.option("-r", "--relative", is_flag=True, help="Specify that the provided path is relative.")
def main(path, absolute, relative):
    """
    Scaffold a Flask project.

    -pa, --path: The base directory where the project should be scaffolded.
    -a, --absolute: Specify that the provided path is absolute.
    -r, --relative: Specify that the provided path is relative.
    """
    # Validate mutually exclusive options
    if absolute and relative:
        raise click.UsageError("Options --absolute and --relative are mutually exclusive.")
    if not absolute and not relative:
        raise click.UsageError("You must specify either --absolute or --relative.")
    
    # Resolve the base path based on the type
    base_path = Path(path).resolve() if type == "absolute" else Path(os.getcwd()) / path

    # Ensure the base path exists
    os.makedirs(base_path, exist_ok=True)

    # Create the folder structure
    create_structure(base_path, FOLDER_STRUCTURE)
    print(f"Project scaffolded at: {base_path}")

if __name__ == "__main__":
    main()
