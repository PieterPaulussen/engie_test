import numpy as np


def test_01_filter_int(client):
    """Test the filter endpoint with a predefined list of integers."""
    values = [17, 15, 7, 5, 29, 36, 4, 1, 3]
    response = client.post("/filter", json=values)
    assert response.status_code == 200
    assert response.json == [36, 15, 3]


def test_02_filter_float(client):
    """Test the filter endpoint with a predefined list of floating point numbers."""
    values = [17.2, 15.0, 7.8, 5.3, 27.1, 36.0, 4.1, 1.0, 3.0]
    response = client.post("/filter", json=values)
    assert response.status_code == 200
    assert response.json == [36.0, 15.0, 3.0]


def test_03_filter_mixed(client):
    """
    Test the filter endpoint with a predefined list of mixed integers and floating
    point numbers.
    A validation error is expected because the list is not homogeneous.
    """
    values = [17.2, 15.0, 7, 5, 27.1, 36, 4.1, 1.0, 3.0]
    response = client.post("/filter", json=values)
    assert response.status_code == 400
    assert "validation_error" in response.json


def test_04_filter_empty(client):
    """Test the filter endpoint with an empty list."""
    values = []
    response = client.post("/filter", json=values)
    assert response.status_code == 200
    assert response.json == []


def test_05_filter_random_integers(client):
    """Test the filter endpoint with a random list of integers.

    Mainly used to assess the performance of the filter and sort operation.
    """
    rng = np.random.default_rng()
    values = rng.integers(low=-1000000, high=1000000, size=1000000).tolist()
    response = client.post("/filter", json=values)
    assert response.status_code == 200


def test_06_filter_random_floats(client):
    """Test the filter endpoint with a random list of floating point numbers.

    Mainly used to assess the performance of the filter and sort operation.
    """
    rng = np.random.default_rng()
    values = rng.uniform(low=-1000000, high=1000000, size=1000000).tolist()
    response = client.post("/filter", json=values)
    assert response.status_code == 200
