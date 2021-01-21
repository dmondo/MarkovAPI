"""Flask app and routes."""
from typing import Any

from flask import Flask, jsonify

from src.helpers import markov

app = Flask(__name__)


@app.route("/model")
def markov_api_route() -> Any:
    """GET route for markov model.

    Returns:
        JSON representation of markov model.
    """
    test_data = ["sample text"]
    model = markov.build_model(test_data, 3)
    return jsonify(model)
