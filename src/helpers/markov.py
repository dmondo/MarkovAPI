"""Helper functions to build Markov model."""

import re
from typing import Dict, List


def build_model(text_data: List[str], order: int) -> Dict[str, List[str]]:
    """Build n-grams markov model of order n from text.

    Args:
        text_data: A list of texts passed to the API.
        order: The order of the n-grams model to build.

    Returns:
        An n-gram markov model of the specified order.
    """
    model: Dict[str, List[str]] = {}

    for corpus in text_data:
        text = re.sub(r"[^A-Za-z0-9 ]+", "", corpus).split(" ")

        for i in range(len(text) - order):
            n_gram = " ".join(text[i : i + order])

            if n_gram not in model:
                model[n_gram] = []
            model[n_gram].append(text[i + order])

    return model
