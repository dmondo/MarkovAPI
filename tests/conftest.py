"""Fixtures for pytest suite."""


from flask.testing import FlaskClient
import pytest

from src.markov_api import app


@pytest.fixture
def client() -> FlaskClient:
    """A mock API client."""
    return app.app.test_client()
