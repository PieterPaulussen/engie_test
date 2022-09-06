# Engie Test

This repository contains the code for the Engie test that was provided during the
technical interview.

## The task description

Create a REST API with one endpoint `/filter` expecting a JSON body containing a list 
of numbers (any type of numbers).
1. Return a JSON response containing a list based on the provided input list (consider
   that this list could contain thousands of records).
2. The JSON response can only contain the values of the input list which are a multiple 
   of 3. 
3. Additionally, the response list should be reversely sorted. 
4. The project does not  need to contain the whole setup to make it deployable.
   However, in addition to the code of the application, it should contain a test suite 
   ensuring that those specifications are matched.

### Exaples
Below is a sample API request with the expected response (HTTP 200):

#### Example 1
POST `/filter`
```
[17, 15, 7, 5, 29, 36 , 4 , 1, 3]
```

Response:
```
[36, 15, 3]
```

#### Example 2
POST `/filter`
```
[17.2, 15.0, 7.8, 5.3, 27.1, 36.0 , 4.1 , 1.0, 3.0]
```

Response:
```
[36.0, 15.0, 3.0]
```


This repository contains the necessary basic layout for a Python project including a 
pre-commit configuration to ensure the code conventions are applied.

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


## Start the development server

```bash
flask --app core/main.py --debug run
```

## Testing

The unit tests can be run with the following command:

```bash
pytest
```
