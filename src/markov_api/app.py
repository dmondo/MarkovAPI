"""Flask app and routes."""
from typing import Any

from flask import Flask, jsonify

from src.helpers import markov

app = Flask(__name__)


@app.route("/model")
def get_markov_model() -> Any:
    """GET route for markov model.

    Returns:
        JSON representation of markov model.
    """
    test_data = ["this is some sample text"]
    model = markov.build_model(text_data=test_data, order=3)
    return jsonify(model)


@app.route("/chain")
def get_markov_chain() -> Any:
    """GET chain from param model.

    Returns:
        JSON representation of markov chain.
    """
    test_model = {
        "This is": ["some"],
        "is some": ["is", "sample"],
        "some is": ["some"],
        "some sample": ["text"],
    }
    chain = markov.generate_chain(model=test_model, length=15, order=3)
    return jsonify(chain)
