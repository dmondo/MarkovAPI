import pytest
from src.markov_api import app

@pytest.fixture
def client():
    return app.app.test_client()
