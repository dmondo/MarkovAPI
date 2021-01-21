"""API route tests."""
from flask.testing import FlaskClient


def test_app_route_returns_model(client: FlaskClient) -> None:
    """It returns 200 and a markov model object."""
    response = client.get("/model")
    assert response.status_code == 200
