from flask import Flask

from src.helpers import markov

app = Flask(__name__)

@app.route('/')
def markov_api_route():
    model = markov.build_model()
    return model

if __name__ == '__main__':
    app.run(debug=True)
