"""API route tests."""
from flask.testing import FlaskClient


def test_app_chain_route_returns_chain(client: FlaskClient) -> None:
    """It returns 200 and a markov chain object."""
    payload = {
        "text": ["This is some sample text"],
        "order": 3,
        "length": 10,
        "num_chains": 2,
    }
    response = client.post("/chains", json=payload)
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
