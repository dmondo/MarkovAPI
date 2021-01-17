from flask.testing import FlaskClient
import pytest

from src.markov_api import app


@pytest.fixture
def client() -> FlaskClient:
    return app.app.test_client()
