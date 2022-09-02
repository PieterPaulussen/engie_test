# Template repository for Python 3.10

This template repository contains the necessary basic layout to create a Python project including a pre-commit configuration to ensure the code conventions are applied.

## Installation and configuration

### Prerequisites
Ensure you have python 3.10,  virtualenv and poetry installed and available in your path.

### Install the python dependencies
Create a new repository from this template and install the Python dependencies.
  ```bash
  virtualenv -p python3.10 venv
  source venv/bin/activate
  poetry install
  ```

## Adding new depencies

```bash
poetry add <python dependency>
```
