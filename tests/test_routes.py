"""API route tests."""
import json
from unittest import TestCase

from flask.testing import FlaskClient


def test_app_model_route_returns_model(client: FlaskClient) -> None:
    """It returns 200 and a markov model object."""
    response = client.get("/model")
    data = json.loads(response.get_data())
    expected_model = {"is some sample": ["text"], "this is some": ["sample"]}

    assert response.status_code == 200
    TestCase().assertDictEqual(data, expected_model)


def test_app_chain_route_returns_chain(client: FlaskClient) -> None:
    """It returns 200 and a markov chain object."""
    response = client.get("/chain")
    data = json.loads(response.get_data())

    assert response.status_code == 200
    assert isinstance(data, str)
