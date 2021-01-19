"""Flask app and routes."""

from flask import Flask

from src.helpers import markov

app = Flask(__name__)


@app.route("/")
def markov_api_route() -> str:
    """GET route for markov model.

    Returns:
        Str representation of markov model.
    """
    model = markov.build_model()
    return model
