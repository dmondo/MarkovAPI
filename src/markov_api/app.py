from flask import Flask

from src.helpers import markov

app = Flask(__name__)


@app.route("/")
def markov_api_route() -> str:
    model = markov.build_model()
    return model
