"""Flask app and routes."""
import json
from typing import Any

from flask import Flask, jsonify, request
from flask_cors import CORS

from src.helpers import markov

app = Flask(__name__)
CORS(app)


@app.route("/chains", methods=["POST"])
def get_markov_model() -> Any:
    """POST route for markov model.

    Returns:
        JSON representation of markov model.
    """
    params = json.loads(request.get_data())
    text_data = params.get("text", [""])
    order = params.get("order", 3)
    length = params.get("length", 10)
    num_chains = params.get("num_chains", 1)

    model = markov.build_model(text_data=text_data, order=order)
    chains = markov.generate_chains(
        model=model, length=length, order=order, num_chains=num_chains
    )

    return jsonify(chains)
